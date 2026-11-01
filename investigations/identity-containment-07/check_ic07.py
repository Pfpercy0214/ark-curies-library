#!/usr/bin/env python3
"""IC-07: conditional closed-field/exchange calculations; no experimental fit.
Run with Python 3.11+, numpy, scipy, sympy:
  OPENBLAS_NUM_THREADS=1 python check_ic07.py --output test-results.json
The dimensionless double well is inherited as a candidate from IC-06.
Conserved integral and exchange kinetics are additional declared assumptions.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import platform
import numpy as np
import scipy
from scipy.integrate import cumulative_trapezoid, simpson, solve_bvp, solve_ivp
from scipy.linalg import cholesky, eigh, eigvalsh, null_space, solve
from scipy.sparse import bmat, csr_matrix, diags
from scipy.sparse.linalg import LinearOperator, eigsh, spsolve
import sympy as sp

CHECKS=[]

def require(ok, message):
    if not bool(ok): raise AssertionError(message)

def record(name, fn):
    try:
        CHECKS.append(dict(name=name, status='PASS', detail=fn()))
    except Exception as exc:
        CHECKS.append(dict(name=name, status='FAIL', error=repr(exc)))

class Cell:
    """Spherical finite-volume discretization; regular center and no field flux."""
    def __init__(self, n=200, L=20.0, mean=-0.75):
        if n<20 or L<=0 or not -1<mean<1: raise ValueError('Invalid cell')
        self.n=n; self.L=L; self.mean=mean; self.h=L/n
        self.edges=np.linspace(0,L,n+1)
        self.r=(self.edges[:-1]+self.edges[1:])/2
        self.w=4*np.pi/3*np.diff(self.edges**3); self.W=self.w.sum()
        self.c=4*np.pi*self.edges[1:-1]**2/self.h
        self.G=(diags(np.r_[self.c,0]+np.r_[0,self.c],0)
                -diags(self.c,1)-diags(self.c,-1)).tocsr()
        self.A=diags(1/self.w)@self.G
        self.sqrtw=np.sqrt(self.w); self.s=self.sqrtw/np.sqrt(self.W)
    def mu(self,q): return self.A@q+q*(q*q-1)
    def energy(self,q):
        return float(np.dot(self.c,np.diff(q)**2)/2+
                     np.dot(self.w,(q*q-1)**2)/4)
    def hessian(self,q):
        inv=1/self.sqrtw
        return (diags(inv)@self.G@diags(inv)+diags(3*q*q-1)).tocsr()
    def stationary(self, mean=None, guess=None):
        m=self.mean if mean is None else mean
        if guess is None:
            q=np.tanh((self.L*((m+1)/2)**(1/3)-self.r)/np.sqrt(2))
            q+=m-np.dot(self.w,q)/self.W; mu=0.1
        else: q=np.array(guess[0],copy=True); mu=float(guess[1])
        for it in range(60):
            e=np.r_[self.mu(q)-mu,np.dot(self.w,q)/self.W-m]
            if max(abs(e))<2e-10: break
            H=self.A+diags(3*q*q-1)
            J=bmat([[H,csr_matrix(-np.ones((self.n,1)))],
                    [csr_matrix((self.w/self.W).reshape(1,-1)),csr_matrix((1,1))]],format='csr')
            d=spsolve(J,-e); step=1.0
            while step>1e-8:
                qn=q+step*d[:-1]; mun=mu+step*d[-1]
                en=np.r_[self.mu(qn)-mun,np.dot(self.w,qn)/self.W-m]
                if np.linalg.norm(en)<np.linalg.norm(e): break
                step*=0.5
            if step<=1e-8: raise RuntimeError('Newton line search stalled')
            q,mu=qn,mun
        else: raise RuntimeError('Newton iteration limit')
        require(np.max(abs(e))<2e-10,'Stationary residual')
        return q,mu,it,float(np.max(abs(e)))
    def spectra(self,q):
        H=self.hessian(q)
        start=np.sin(self.r)+0.2
        free=eigsh(H,k=3,which='SA',tol=1e-10,v0=start,return_eigenvectors=False)
        def P(x): return x-self.s*np.dot(self.s,x)
        op=LinearOperator((self.n,self.n),matvec=lambda x:P(H@P(x))+100*self.s*np.dot(self.s,x))
        ev,vec=eigsh(op,k=3,which='SA',tol=1e-10,v0=P(start))
        require(np.max(abs(self.s@vec))<1e-8,'Projected mode violates constraint')
        angular={}
        for l in (1,2):
            angular[str(l)]=float(eigsh(H+diags(l*(l+1)/self.r**2),k=1,
                               which='SA',tol=1e-10,v0=start,return_eigenvectors=False)[0])
        return sorted(free.tolist()),sorted(ev.tolist()),angular
    def mobility(self,g=0.0):
        if g<0: raise ValueError('Negative boundary conductance')
        B=self.G.copy().tolil(); B[-1,-1]+=g
        return B.tocsr()
    def dynamic_top(self,q,g):
        inv=1/self.sqrtw
        D=(diags(inv)@self.mobility(g)@diags(inv)).toarray()
        H=self.hessian(q).toarray()
        C=cholesky(D,lower=True)
        val,vec=eigh(-C.T@H@C,subset_by_index=(self.n-1,self.n-1))
        y=C@vec[:,0]; y/=np.linalg.norm(y)
        return float(val[0]),y


def reciprocal_conservation():
    weights=np.array([[0,1,0.2],[1,0,0.7],[0.2,0.7,0.]])
    q=np.array([0.1,0.8,-0.2])
    rhs=lambda w: (w*(q[None,:]-q[:,None])).sum(axis=1)
    good=float(rhs(weights).sum());weights[0,1]+=0.3
    bad=float(rhs(weights).sum())
    require(abs(good)<1e-14 and abs(bad)>0.01,'Reciprocity control failed')
    return dict(reciprocal_sum=good,asymmetric_sum=bad,
                limitation='Source E1 conservation needs reciprocal weights, common eta, no drive and closed links')

cells={};solutions={};summaries=[]
def grid_study():
    for n in (100,200,400,800):
        c=Cell(n);q,mu,it,res=c.stationary();cells[n]=c;solutions[n]=(q,mu)
        free,con,angular=c.spectra(q)
        z=np.flatnonzero(q[:-1]*q[1:]<0)
        require(len(z)==1,'Not a single radial interface')
        j=z[0];R=float(c.r[j]+c.h*q[j]/(q[j]-q[j+1]))
        row=dict(cells=n,mean=float(c.w@q/c.W),mu=mu,residual=res,iterations=it,
                 radius=R,energy=c.energy(q),uniform_energy=c.energy(np.full(n,c.mean)),
                 radial_free_lowest=free[0],radial_constrained_lowest=con[0],angular_lowest=angular)
        require(abs(row['mean']-c.mean)<1e-12,'Mean drift')
        require(free[0]<-0.02 and con[0]>0.20,'Radial sign control failed')
        require(row['energy']<row['uniform_energy'],'Uniform comparator lower in this chosen example')
        summaries.append(row)
    ratios=[(summaries[i]['energy']-summaries[i-1]['energy'])/
            (summaries[i+1]['energy']-summaries[i]['energy']) for i in (1,2)]
    require(all(3.8<r<4.2 for r in ratios),'Energy grid differences not second order')
    require(summaries[-1]['angular_lowest']['1']<summaries[0]['angular_lowest']['1']/50,
            'Nearly translational sector did not approach zero')
    return dict(grids=summaries,energy_refinement_ratios=ratios,
                limit='Radial constrained local stability only; no continuum translation pinning or global 3D minimum claimed')


def derivative_checks():
    c=cells[200];q,mu=solutions[200]
    d=np.exp(-((c.r-9)/2)**2);d-=c.w@d/c.W;d/=np.linalg.norm(c.sqrtw*d)
    qtest=q+0.03*np.cos(c.r/3)
    analytic=float(np.dot(c.w*c.mu(qtest),d))
    errors=[abs((c.energy(qtest+e*d)-c.energy(qtest-e*d))/(2*e)-analytic) for e in (.2,.1,.05)]
    require(errors[-1]<errors[0]/10,'First variation nonconvergence')
    hquad=float((c.sqrtw*d)@(c.hessian(q)@(c.sqrtw*d)))
    numeric=(c.energy(q+.02*d)-2*c.energy(q)+c.energy(q-.02*d))/.02**2
    require(abs(numeric-hquad)<1e-5,'Hessian energy mismatch')
    return dict(first_variation_errors=errors,hessian_quadratic=hquad,energy_second_difference=numeric)


def independent_bvp():
    c=cells[800];q,mu=solutions[800]
    x=np.linspace(0,c.L,500);guess=np.tanh((9.1-x)/np.sqrt(2))
    y=np.array([guess,-(1-guess*guess)/np.sqrt(2),
                cumulative_trapezoid(4*np.pi*x*x*guess,x,initial=0)])
    def fun(x,y,p): return np.array([y[1],y[0]*(y[0]*y[0]-1)-p[0],4*np.pi*x*x*y[0]])
    def bc(ya,yb,p): return np.array([ya[1],yb[1],ya[2],yb[2]-c.W*c.mean])
    S=np.zeros((3,3));S[1,1]=-2
    sol=solve_bvp(fun,bc,x,y,p=[.1],S=S,tol=1e-8,max_nodes=20000)
    require(sol.success,sol.message)
    xx=np.linspace(0,c.L,20001);yy=sol.sol(xx)
    E=float(simpson(4*np.pi*xx**2*(yy[1]**2/2+(yy[0]**2-1)**2/4),x=xx))
    require(abs(float(sol.p[0])-mu)<2e-6,'BVP/FV chemical response mismatch')
    require(abs(E-c.energy(q))<0.02,'BVP/FV energy mismatch')
    return dict(method='independent continuous radial boundary-value collocation',mu=float(sol.p[0]),
                energy=E,nodes=len(sol.x),max_rms_residual=float(max(sol.rms_residuals)),
                mu_difference=float(sol.p[0]-mu),energy_difference=E-c.energy(q))


def budgets():
    c=cells[100];q,mu0=solutions[100]
    x=q+.01*np.cos(c.r);mu=c.mu(x);g=3.;B=c.mobility(g)
    rhs=-(B@(mu-mu0))/c.w
    balance=float(c.w@rhs+g*(mu[-1]-mu0))
    grandrate=float((c.w*(mu-mu0))@rhs)
    diss=-float(np.dot(c.c,np.diff(mu)**2)+g*(mu[-1]-mu0)**2)
    closed=-(c.G@mu)/c.w
    require(abs(balance)<1e-9 and abs(grandrate-diss)<1e-9,'Boundary energy/content budget')
    require(abs(c.w@closed)<1e-9 and grandrate<0,'Conservation/dissipation failure')
    return dict(content_balance_error=balance,grand_energy_rate=grandrate,dissipation=diss,
                closed_content_rate=float(c.w@closed))


def susceptibility_and_leakage():
    c=cells[200];q,mu0=solutions[200];H=c.hessian(q).toarray()
    susceptibility=float(c.sqrtw@solve(H,c.sqrtw,assume_a='sym'))
    dm=1e-6
    qm,mum,_,_=c.stationary(mean=c.mean-dm,guess=(q,mu0))
    qp,mup,_,_=c.stationary(mean=c.mean+dm,guess=(q,mu0))
    fd=2*dm*c.W/(mup-mum)
    require(susceptibility<0 and abs(fd/susceptibility-1)<1e-5,'Susceptibility mismatch')
    rates=[]
    for g in (10.,1.,.1):
        rate,_=c.dynamic_top(q,g)
        require(rate>0,'Open system lacks expected growing radial mode')
        rates.append(dict(conductance=g,growth_rate=rate,rate_over_g=rate/g))
    limit=-1/susceptibility
    require(abs(rates[-1]['rate_over_g']/limit-1)<0.003,'Weak exchange limit inaccurate')
    require(abs(rates[-1]['rate_over_g']/limit-1)<abs(rates[0]['rate_over_g']/limit-1),
            'Exchange limit did not improve')
    return dict(dC_dmu=susceptibility,independent_branch_difference=fd,
                weak_exchange_limit_rate_over_g=limit,rates=rates,
                interpretation='An e-folding rate in declared units, not a stochastic or measured particle lifetime')


def finite_environment():
    c=cells[200];q,_=solutions[200];H=c.hessian(q).toarray();r=c.sqrtw
    beta_crit=-1/float(r@solve(H,r,assume_a='sym'))
    vals=[]
    for factor in (0.,.9,1.,1.1,2.):
        lam=float(eigvalsh(H+factor*beta_crit*np.outer(r,r),subset_by_index=(0,0))[0])
        vals.append(dict(beta_over_threshold=factor,lowest_radial_curvature=lam))
    require(vals[1]['lowest_radial_curvature']<0 and vals[3]['lowest_radial_curvature']>0,
            'Finite environment failed to change radial stability')
    require(abs(vals[2]['lowest_radial_curvature'])<1e-9,'Threshold not marginal')
    return dict(beta_threshold=beta_crit,cases=vals,
                provenance='Quadratic Taylor response of finite reservoir; additional measurable/derivable input, not a fitted rescue')


def nonlinear_evolution():
    c=cells[100];q,mu0=solutions[100];H=c.hessian(q).toarray()
    # Close the cell: initial disturbance has exactly zero integrated amount.
    d=np.exp(-((c.r-9)/2)**2);d-=c.w@d/c.W;d/=max(abs(d))
    qinit=q+1e-3*d
    def run(g,x0,tf):
        B=c.mobility(g);Jleft=-diags(1/c.w)@B
        def rhs(t,x): return Jleft@(c.mu(x)-mu0)
        def jac(t,x): return Jleft@(c.A+diags(3*x*x-1))
        out=solve_ivp(rhs,(0,tf),x0,method='BDF',jac=jac,rtol=1e-9,atol=1e-11,
                      t_eval=np.linspace(0,tf,41))
        require(out.success,out.message)
        return out
    closed=run(0.,qinit,100.)
    masses=c.w@closed.y
    energies=np.array([c.energy(x) for x in closed.y.T])
    dist=lambda x:float(np.linalg.norm(c.sqrtw*(x-q)))
    require(np.max(abs(masses-masses[0]))<1e-8,'Nonlinear closed cell leaks')
    require(max(np.diff(energies))<1e-7 and dist(closed.y[:,-1])<dist(qinit),
            'Closed disturbance failed to relax')
    rate,y=c.dynamic_top(q,100.);d=y/c.sqrtw;d/=max(abs(d))
    x0=q+1e-5*d;tf=.3/rate
    opened=run(100.,x0,tf)
    ratio=dist(opened.y[:,-1])/dist(x0)
    grand=np.array([c.energy(x)-mu0*(c.w@x) for x in opened.y.T])
    require(ratio>1.2 and abs(ratio/np.exp(.3)-1)<.01,'Nonlinear growth/eigenvalue disagreement')
    require(max(np.diff(grand))<1e-6,'Open grand energy increased')
    return dict(closed_mass_max_drift=float(max(abs(masses-masses[0]))),
                closed_initial_distance=dist(qinit),closed_final_distance=dist(closed.y[:,-1]),
                open_time=tf,open_rate=rate,open_measured_amplification=ratio,
                linear_expected_amplification=float(np.exp(.3)),
                open_amount_change=float(c.w@(opened.y[:,-1]-x0)))


def capillary_limit():
    R,N,sigma,p0=sp.symbols('R N sigma p0',positive=True)
    V=4*sp.pi*R**3/3;n=N/V;f=sp.Function('f')
    E=4*sp.pi*sigma*R**2+V*f(n)+p0*V
    x=sp.symbols('x',positive=True)
    p=x*sp.diff(f(x),x)-f(x);B=x*x*sp.diff(f(x),x,2)
    eq=4*sp.pi*R**2*(p0-p.subs(x,n)+2*sigma/R)
    require(sp.simplify(sp.diff(E,R)-eq)==0,'Pressure balance derivation')
    curvature=sp.diff(E,R,2).subs(p0,p.subs(x,n)-2*sigma/R)
    require(sp.simplify(curvature-4*sp.pi*R*(3*B.subs(x,n)-2*sigma/R))==0,'Bulk response criterion')
    return dict(criterion='3B > 2 sigma/R for radial minimum at fixed N and constant sigma',
                limit='Thin interface, specified fixed temperature/entropy path, homogeneous interior; separate coarse comparator')


def closed_linear_spectrum():
    c=cells[100];q,_=solutions[100];H=c.hessian(q).toarray()
    Q=null_space(c.s.reshape(1,-1))
    inv=1/c.sqrtw;D=inv[:,None]*c.G.toarray()*inv[None,:]
    Hp=Q.T@H@Q;Dp=Q.T@D@Q
    C=cholesky(Dp,lower=True)
    top=float(eigvalsh(-C.T@Hp@C,subset_by_index=(c.n-2,c.n-2))[0])
    require(top<0,'Conserved radial dynamics unstable')
    return dict(slowest_radial_growth_exponent=top,
                limitation='Overdamped relaxation exponent; not omega, a clock frequency, or a universal speed')


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',default='test-results.json')
    args=parser.parse_args()
    for name,fn in [
        ('source_reciprocity_and_conservation',reciprocal_conservation),
        ('spherical_stationary_grid_and_radial_stability',grid_study),
        ('independent_energy_variations',derivative_checks),
        ('continuous_boundary_value_cross_check',independent_bvp),
        ('content_and_grand_energy_budgets',budgets),
        ('conserved_radial_dynamic_spectrum',closed_linear_spectrum),
        ('weak_exchange_and_susceptibility',susceptibility_and_leakage),
        ('finite_environment_restoring_response',finite_environment),
        ('nonlinear_relaxation_and_exchange_growth',nonlinear_evolution),
        ('capillary_pressure_response_limit',capillary_limit)]:
        record(name,fn)
    report=dict(study='IC-07',utc=datetime.now(timezone.utc).isoformat(),
                python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__,sympy=sp.__version__,
                script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                passed=sum(c['status']=='PASS' for c in CHECKS),total=len(CHECKS),checks=CHECKS,
                limitations=['No empirical data or ARK scalar identification','Finite-cell spherical/radial calculation',
                             'No claim of global or unrestricted three-dimensional stability',
                             'Conserved integral and reservoir mobility require physical derivation',
                             'No independent second reviewer; alternative solvers are implementation checks'])
    Path(args.output).write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))
    return 0 if report['passed']==report['total'] else 1

if __name__=='__main__': raise SystemExit(main())
