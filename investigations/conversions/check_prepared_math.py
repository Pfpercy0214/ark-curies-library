#!/usr/bin/env python3
"""Read-only math syntax check for prepared papers; not source-fidelity certification."""
from pathlib import Path
import hashlib,json,re,subprocess,xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[2]
rows=[]
for item in json.loads((R/'history/ingestion/prepared-papers.json').read_text()):
 p=R/item['path'];run=subprocess.run(['pandoc',str(p),'-f','markdown','-t','html5','--mathml'],capture_output=True,text=True,check=True)
 nodes=re.findall(r'<math\b.*?</math>',run.stdout,re.S)
 for node in nodes:
  ET.fromstring(node)
  assert '<merror' not in node,item['path']
 assert not run.stderr,(item['path'],run.stderr)
 rows.append(dict(paper=item['paper'],path=item['path'],sha256=hashlib.sha256(p.read_bytes()).hexdigest(),mathml_nodes=len(nodes),status='PASS_SYNTAX_ONLY'))
print(json.dumps({'scope':'Pandoc MathML syntax, not scientific or source-fidelity validation; literal source math is intentionally not counted as encoded math.', 'papers':rows},indent=2))
