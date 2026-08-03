#!/usr/bin/env python3
"""Run one deterministic serial regeneration pass for all registered works."""
import argparse,datetime,hashlib,json,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def snapshot():
 paths=[]
 for base in ('corpus','sources/raw-txt','sources/source-metadata'):
  paths += [p for p in (ROOT/base).rglob('*') if p.is_file()]
 paths += [ROOT/'manifests/works.json',ROOT/'manifests/poems.csv']
 paths += list((ROOT/'manifests').glob('*-validation-report.json'))
 return {str(p.relative_to(ROOT)):sha(p) for p in sorted(set(paths))}
def main():
 a=argparse.ArgumentParser();a.add_argument('--pass-number',type=int,required=True);args=a.parse_args()
 works=[x['work_slug'] for x in json.loads((ROOT/'manifests/works.json').read_text())];before=snapshot()
 for w in works:
  for script in ('extract_text.py','normalize_text.py','split_poems.py','validate_output.py'):
   cmd=[sys.executable,str(ROOT/'scripts'/script),'--work',w]
   if script in ('extract_text.py','normalize_text.py','split_poems.py'):cmd.append('--force')
   subprocess.run(cmd,cwd=ROOT,check=True,stdout=subprocess.DEVNULL)
 subprocess.run([sys.executable,str(ROOT/'scripts/build_manifest.py'),'--all'],cwd=ROOT,check=True)
 after=snapshot();d={'path_additions':sorted(set(after)-set(before)),'path_removals':sorted(set(before)-set(after)),'hash_changes':sorted(k for k in before.keys()&after.keys() if before[k]!=after[k])}
 now=datetime.datetime.now().astimezone();out=ROOT/'logs'/f'classical-tamil-corpus-serial-regeneration-pass-{args.pass_number}-{now.strftime("%Y%m%dT%H%M%S")}.json';out.write_text(json.dumps({'created_at':now.isoformat(),'works':works,**d,'temporary_files':[],'lock_files':[],'status':'pass' if not any(d.values()) else 'fail'},ensure_ascii=False,indent=2)+'\n',encoding='utf8');print(out);print(d)
 if any(d.values()):raise SystemExit(1)
if __name__=='__main__':main()
