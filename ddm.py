#! /usr/bin/env python3

import excel
import json

wb = excel.open('ddm.xls')
sh = wb[0]

d = {}
for r in sh.rows:
  l = r[3].value
  s = r[7].value
  d[l] = s
  print(l,s)

j = 'var DDM = '
s = json.dumps(d,sort_keys=True,indent=4)
f = open('ddm.js', 'w')
f.write(j + s)