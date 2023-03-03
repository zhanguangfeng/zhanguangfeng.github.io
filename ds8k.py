#! /usr/bin/env python3

import excel
import json

wb = excel.open('ds8k.xlsx')
sh = wb[0]

r = 0
l = len(sh)
h = {}

name = None
while r < l:
  r += 1
  a = sh[r][1].value
  if a and a.startswith('DS'):
    name = a
    h[name] = {'Enclosure': [], 'Location': [], 'Frames': []}
    continue
  elif a and a > u'\u4e000':
    continue
  elif a:
    h[name]['Enclosure'].append(a)

  b = sh[r][2].value
  if b:
    h[name]['Location'].append(b)
  
  c = sh[r][3].value
  if c:
    h[name]['Frames'].append({'M/T': c})
  
  d = sh[r][4].value
  if d:
    h[name]['Frames'][-1]['S/N'] = d.upper()

a = []
for name, data in h.items():
  encls = data['Enclosure']
  locs = data['Location']
  ie = len(encls)
  il = len(locs)
  if ie != il: print('ie != il')
  i = 0
  while i < ie:
    enclnum = encls[i]
    enclloc = locs[i]
    if '/R1-S' in enclnum:
      mt = data['Frames'][0]['M/T'].upper()
      sn = data['Frames'][0]['S/N'].upper()
    else:
      mt = data['Frames'][1]['M/T'].upper()
      sn = data['Frames'][1]['S/N'].upper()

    a.append({'NAME': name, 'M/T': mt, 'S/N': sn, 'ENCLNUM': enclnum, 'ENCLLOC': enclloc})
    print(name, mt,sn,enclnum,enclloc,sep="\t")
    i += 1

j = 'var ds8k = '
s = json.dumps(a,sort_keys=True,indent=4)
f = open('ds8k.js', 'w')
f.write(j + s)