#!/usr/bin/env python3
import argparse, json, math, statistics
from pathlib import Path
NAME='001-json-validator'
DESC='تحقق JSON'
def main():
 p=argparse.ArgumentParser(description=DESC)
 p.add_argument('--values', nargs='*', type=float, default=[])
 p.add_argument('--input'); p.add_argument('--output')
 a=p.parse_args(); vals=a.values
 if a.input:
  text=Path(a.input).read_text(encoding='utf-8', errors='replace')
  nums=[]
  for x in text.replace(',', ' ').split():
   try: nums.append(float(x))
   except ValueError: pass
  vals=nums
 result={'tool':NAME,'description':DESC,'count':len(vals),'sum':sum(vals),'min':min(vals) if vals else None,'max':max(vals) if vals else None,'mean':statistics.mean(vals) if vals else None}
 if not vals: result['note']='Educational offline calculator. Provide numeric --values or --input when applicable.'
 out=json.dumps(result,ensure_ascii=False,indent=2)
 if a.output: Path(a.output).write_text(out+'\n',encoding='utf-8')
 else: print(out)
if __name__=='__main__': main()
