#! /usr/bin/env python3

import excel
import json

wb = excel.open('ddm.xlsx')
sh = wb[0]
js = None
with open('ddm.js') as fp:
    tmp, jss = fp.read().split('=')
    js = json.loads(jss)

d = {}
a = []
for r in sh.rows:
    l = r[3].value
    s = r[7].value
    d[l] = s
    v = js[l]
    if v != s:
        a.append( '{:24}: \033[31m{}\033[0m -> \033[32m{}\033[0m'.format(l, v, s) )
    else:
        print( '{:24}: {}'.format(l, s) )

if a: print('-' * 31)
for s in a:
    print(s)
j = 'var ddm = '
s = json.dumps(d, sort_keys=True, indent=4)
f = open('ddm.js', 'w')
f.write(j + s)
