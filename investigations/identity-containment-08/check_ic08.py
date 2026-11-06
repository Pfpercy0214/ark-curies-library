#!/usr/bin/env python3
"""IC-08: amount, phase winding, and conditional superfluid response.
Conventional Gross-Pitaevskii comparator; no ARK identification or data fit.
Python 3.11+; numpy, scipy, sympy. All computed examples are dimensionless.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import platform
from datetime import datetime, timezone
import numpy as np
import scipy
from scipy.integrate import quad
import sympy as sp

CHECKS = []
def require(ok, message):
    if not bool(ok):
        raise AssertionError(message)
def record(name, function):
    try:
        CHECKS.append(dict(name=name, status='PASS', detail=function()))
    except Exception as exc:
        CHECKS.append(dict(name=name, status='FAIL', error=repr(exc)))
def grid(n):
    return 2*np.pi*np.arange(n)/n
def deriv(f, order=1):
    k = np.fft.fftfreq(len(f), d=1/len(f))
    return np.fft.ifft((1j*k)**order*np.fft.fft(f))
def norm(psi):
    return float(2*np.pi*np.mean(np.abs(psi)**2))
def energy(psi, V=0.0, g=4.0):
    n = np.abs(psi)**2
    return float(2*np.pi*np.mean(0.5*np.abs(deriv(psi))**2 + .5*g*n*n + V*n))
def winding(psi):
    if np.min(np.abs(psi)) < 1e-9:
        raise ValueError('Phase undefined at a zero: winding not assigned')
    jumps = np.angle(np.roll(psi,-1)*np.conj(psi))
    if np.max(np.abs(jumps)) >= .8*np.pi:
        raise ValueError('Unresolved phase increment: refine grid')
    return float(np.sum(jumps)/(2*np.pi))
def split(psi, V, g, dt, steps):
    p = psi.copy().astype(complex)
    k = np.fft.fftfreq(len(p), d=1/len(p))
    linear = np.exp(-.5j*k*k*dt)
    for _ in range(steps):
        p *= np.exp(-.5j*dt*(V+g*np.abs(p)**2))
        p = np.fft.ifft(linear*np.fft.fft(p))
        p *= np.exp(-.5j*dt*(V+g*np.abs(p)**2))
    return p

def network():
    W = np.array([[0,2,1],[2,0,3],[1,3,0]],float)
    q = np.array([.2,.4,.8]); rhs = np.sum(W*(q[None,:]-q[:,None]),axis=1)
    require(abs(np.sum(rhs)) < 1e-14,'reciprocal sum')
    W[0,1] += 1
    directed = np.sum(W*(q[None,:]-q[:,None]),axis=1)
    require(abs(np.sum(directed)) > .1,'directed counterexample')
    reaction = -(q**3-q)
    require(abs(np.sum(reaction)) > .1,'reaction counterexample')
    return dict(reciprocal_rate=float(np.sum(rhs)), directed_rate=float(np.sum(directed)), local_reaction_rate=float(np.sum(reaction)))

def scalar_topology():
    x=grid(1024); th=.3+.1*np.cos(x)
    for t in [0,.25,.75,1]:
        require(abs(winding(np.exp(1j*((1-t)*th+t*.3)))) < 1e-12,'interval contraction')
    require(np.max(np.abs(np.cos(3*(x+2*np.pi))-np.cos(3*x)))<1e-13,'integer cosine periodic')
    require(np.max(np.abs(np.cos(x)-np.cos(-x)))==0,'projection symmetry')
    require(abs(winding(np.exp(1j*x))-1)<1e-12,'positive winding')
    require(abs(winding(np.exp(-1j*x))+1)<1e-12,'negative winding')
    return dict(real_interval_winding=0, complex_projection_identical_for_opposite_windings=True, integer_cosine_rotation='2pi periodic; not a minus sign')

def polar_action():
    n,nx,nxx,h,m,p,px=sp.symbols('n nx nxx h m p px',positive=True)
    grad=h*h*nx*nx/(8*m*n)
    variation=sp.diff(grad,n)-sp.diff(sp.diff(grad,nx),n)*nx-sp.diff(sp.diff(grad,nx),nx)*nxx
    quantum=-h*h/(2*m)*(nxx/(2*n)-nx*nx/(4*n*n))
    require(sp.simplify(variation-quantum)==0,'quantum gradient')
    flow=h*h*n*p*p/(2*m)
    require(sp.simplify(sp.diff(flow,p)/h-h*n*p/m)==0,'phase current')
    # omega^2 derived by eliminating linear density/phase perturbations
    g,n0,k,om=sp.symbols('g n0 k om',positive=True)
    product=(h*n0*k*k/m)*(g/h+h*k*k/(4*m*n0))
    require(sp.simplify(product-(g*n0*k*k/m+h*h*k**4/(4*m*m)))==0,'dispersion')
    return dict(current='hbar*n*grad(phi)/m', quantum_response=str(quantum), dispersion='Omega^2=g*n0*k^2/m+hbar^2*k^4/(4*m^2)')

def continuity():
    x=grid(512); p=1+.12*np.exp(2j*x)+.07*np.exp(-3j*x)
    V=.2*np.cos(x); rhs=-1j*(-.5*deriv(p,2)+(V+4*np.abs(p)**2)*p)
    nt=2*np.real(np.conj(p)*rhs); j=np.imag(np.conj(p)*deriv(p))
    err=float(np.max(np.abs(nt+deriv(j).real)))
    require(err<1e-9,'local flux law')
    require(abs(2*np.pi*np.mean(nt))<1e-12,'closed amount')
    # Explicit sink: i psi_t = ... - i Gamma psi/2, density loss -Gamma*n.
    Gamma=.1*(1+.2*np.cos(x)); rhs2=rhs-.5*Gamma*p
    loss=2*np.real(np.conj(p)*rhs2)-nt
    require(np.max(np.abs(loss+Gamma*np.abs(p)**2))<1e-13,'source law')
    return dict(local_residual=err, closed_amount_rate=float(2*np.pi*np.mean(nt)), sink_rate=float(2*np.pi*np.mean(loss)))

def temporal():
    x=grid(256); plane=np.exp(2j*x)
    end=split(plane,np.zeros_like(x),4,.001,200)
    exact=plane*np.exp(-1j*(2+4)*.2)
    exact_error=float(np.max(np.abs(end-exact))); require(exact_error<1e-11,'plane evolution')
    p=np.sqrt(1+.15*np.cos(x))*np.exp(1j*(x+.12*np.sin(2*x))); V=.2*np.cos(x)
    reference=split(p,V,4,.000125,1600)
    errs=[]; drifts=[]
    for dt,steps in [(.004,50),(.002,100),(.001,200)]:
        out=split(p,V,4,dt,steps)
        errs.append(float(np.sqrt(np.mean(np.abs(out-reference)**2))))
        drifts.append(float(abs(energy(out,V)-energy(p,V))))
        require(abs(norm(out)-norm(p))<1e-11,'norm preservation')
        require(abs(winding(out)-1)<1e-12,'resolved winding persistence')
    require(errs[0]>3.5*errs[1] and errs[1]>3.5*errs[2],'temporal convergence')
    require(drifts[2]<drifts[0],'energy convergence')
    out128=split(np.sqrt(1+.15*np.cos(grid(128)))*np.exp(1j*(grid(128)+.12*np.sin(2*grid(128)))),.2*np.cos(grid(128)),4,.000125,1600)
    spatial=float(np.max(np.abs(out128-reference[::2])))
    require(spatial<1e-9,'spatial resolution')
    return dict(plane_error=exact_error, dt=[.004,.002,.001], L2_errors=errs, energy_drifts=drifts, grid_128_256_difference=spatial)

def conserved_path():
    x=grid(1024); rows=[]
    for t in [0,.25,.49,.5,.51,.75,1]:
        p=((1-t)*np.exp(1j*x)+t)/np.sqrt((1-t)**2+t*t)
        require(abs(norm(p)-2*np.pi)<1e-12,'path amount')
        if t==.5:
            try: winding(p)
            except ValueError: w=None
            else: raise AssertionError('zero must invalidate winding')
        else:
            w=winding(p); require(abs(w-(1 if t<.5 else 0))<1e-12,'path sector')
        rows.append(dict(path_parameter=t, norm=norm(p), minimum_density=float(np.min(np.abs(p)**2)), winding=w, energy=energy(p)))
    require(all(np.isfinite(r['energy']) for r in rows),'finite path energy')
    return dict(path='externally accessible configuration path, NOT a computed dynamical solution or minimum barrier', states=rows)

def ring(npoints, a, w=1, mu=8.0):
    if not 0<=a<1 or not isinstance(w,int): raise ValueError('Require 0<=a<1 and integer winding')
    x=grid(npoints); n=1-a*np.cos(x); j=w*np.sqrt(1-a*a)
    phip=j/n; k=np.fft.fftfreq(npoints,d=1/npoints); mask=k!=0
    coeff=np.fft.fft(phip-w); phase_coeff=np.zeros_like(coeff)
    phase_coeff[mask]=coeff[mask]/(1j*k[mask])
    phi=w*x+np.fft.ifft(phase_coeff).real
    amp=np.sqrt(n); p=amp*np.exp(1j*phi)
    nx=a*np.sin(x); nxx=a*np.cos(x)
    amp_ratio=nxx/(2*n)-nx*nx/(4*n*n)
    V=mu-4*n-.5*phip**2+.5*amp_ratio
    return x,n,j,p,V,phip

def bottleneck():
    rows=[]
    for a in [0,.5,.8,.95]:
        integral=quad(lambda x:1/(1-a*np.cos(x)),0,2*np.pi,epsabs=1e-11,epsrel=1e-11)[0]
        j=2*np.pi/integral; exact=np.sqrt(1-a*a)
        require(abs(j-exact)<1e-12,'inverse-density current')
        vmax=j/(1-a); csmin=2*np.sqrt(1-a)
        flow_energy=(2*np.pi)**2/(2*integral)
        rows.append(dict(depletion=a, current=j, max_velocity=vmax, local_sound_speed_min=csmin, ratio=vmax/csmin, flow_energy=flow_energy))
    require(rows[-1]['current']<rows[0]['current'] and rows[-1]['max_velocity']>rows[0]['max_velocity'],'opposite trends')
    return dict(number='2*pi for every profile', rows=rows, warning='local sound ratio is diagnostic; not a phase-slip threshold prediction')

def stationary():
    rows=[]
    for N in [32,64,128,256]:
        x,n,j,p,V,phip=ring(N,.8)
        residual=-.5*deriv(p,2)+(V+4*n)*p-8*p
        err=float(np.sqrt(np.mean(np.abs(residual)**2)))
        rows.append(dict(grid=N,residual=err))
    require(rows[-1]['residual']<1e-8 and rows[1]['residual']<rows[0]['residual']/10,'manufactured solution convergence')
    x,n,j,p,V,phip=ring(256,.8)
    require(abs(winding(p)-1)<1e-12,'stationary winding')
    require(np.max(np.abs(np.imag(np.conj(p)*deriv(p))-j))<1e-8,'stationary current')
    out=split(p,V,4,.0001,100)
    evo=float(np.max(np.abs(out-p*np.exp(-.08j))))
    require(evo<1e-6,'stationary time evolution')
    V2=ring(256,.8,mu=11)[4]
    require(np.max(np.abs(V2-V-3))<1e-12,'constant potential shift')
    return dict(refinement=rows, time_evolution_error=evo, provenance='density and winding prescribed; potential manufactured from equation, NOT an independent prediction of apparatus response')

def energy_minimum():
    x,n,j,p,V,phip=ring(1024,.8)
    base=float(np.pi*np.mean(n*phip**2)); eps=.2
    extra=2*eps*np.cos(2*x)
    varied=float(np.pi*np.mean(n*(phip+extra)**2))
    expected=float(np.pi*np.mean(n*extra**2))
    require(abs((varied-base)-expected)<1e-12 and varied>base,'fixed-density phase minimum')
    return dict(base=base, varied=varied, increase=varied-base, scope='minimization over phase ONLY at prescribed positive density and winding')

def energetic_vs_dynamic():
    rows=[]; x=grid(8192); eps=1e-5
    for w in [1,3]:
        g=4.; k=1.; M=np.array([[g+k*k/4,w*k],[w*k,k*k]])
        ev,vec=np.linalg.eigh(M); A,B=vec[:,0]
        p0=np.exp(1j*w*x)
        def pert(t): return np.sqrt(1+t*A*np.cos(x))*np.exp(1j*(w*x+t*B*np.sin(x)))
        numeric=(energy(pert(eps))-2*energy(p0)+energy(pert(-eps)))/(eps*eps)
        analytic=np.pi*ev[0]
        require(abs(numeric-analytic)<.02,'energy Hessian finite difference')
        freq=[w-np.sqrt(g+.25),w+np.sqrt(g+.25)]
        require(np.all(np.isreal(freq)),'real Bogoliubov frequencies')
        rows.append(dict(winding=w,lowest_curvature=float(ev[0]),energy_second_difference=float(numeric),analytic_second_difference=float(analytic),frequencies=[float(v) for v in freq]))
    require(rows[0]['lowest_curvature']>0 and rows[1]['lowest_curvature']<0,'energetic threshold')
    return dict(cases=rows, caveat='negative energy direction is not exponential dynamical growth in this lossless model')

def coefficient_identifiability():
    # n0 is measured. Current/winding fixes r=hbar/m; sound fixes s=g/m.
    n0=2.; h=3.; m=4.; g=5.; scale=7.
    def observ(h,m,g): return np.array([h/m,np.sqrt(g*n0/m),np.sqrt((g*n0/m)*.8**2+(h*h/(4*m*m))*.8**4)])
    require(np.max(np.abs(observ(h,m,g)-observ(scale*h,scale*m,scale*g)))<1e-14,'common scaling degeneracy')
    require(abs(.5*h*h/m-.5*(scale*h)**2/(scale*m))>1,'energy breaks scaling with independent units')
    return dict(observables_before=observ(h,m,g).tolist(),observables_after=observ(scale*h,scale*m,scale*g).tolist(),result='velocity and dispersion alone do not determine hbar,m,g separately; energy or another independent anchor is required')

def invalid_inputs():
    for a,w in [(1,1),(-.1,1),(.2,.5)]:
        try: ring(128,a,w)
        except ValueError: pass
        else: raise AssertionError('invalid ring accepted')
    return dict(valid_domain='positive density, integer winding, resolved phase; zeros handled as singular events')

def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--output',default='test-results.json'); args=parser.parse_args()
    for name,fn in [('reciprocal_and_source_balance',network),('real_scalar_vs_phase_topology',scalar_topology),('action_current_and_dispersion',polar_action),('local_continuity_and_sink',continuity),('Hamiltonian_evolution_and_refinement',temporal),('conserved_amount_during_sector_change',conserved_path),('weak_link_inverse_density_response',bottleneck),('manufactured_stationary_ring',stationary),('phase_energy_variation',energy_minimum),('energetic_vs_dynamical_stability',energetic_vs_dynamic),('coefficient_scale_degeneracy',coefficient_identifiability),('invalid_inputs',invalid_inputs)]: record(name,fn)
    report=dict(study='IC-08',utc=datetime.now(timezone.utc).isoformat(),code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__,sympy=sp.__version__,scope='Analytic and generated-data checks only; no experimental fit, independent reviewer, or physical ARK mapping',passed=sum(c['status']=='PASS' for c in CHECKS),total=len(CHECKS),checks=CHECKS)
    Path(args.output).write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))
    raise SystemExit(0 if report['passed']==report['total'] else 1)
if __name__=='__main__': main()
