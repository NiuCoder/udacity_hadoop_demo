#!/usr/bin/env python
import sys
prev_key = None
max_cost = 0
for line in sys.stdin:
    data = line.strip().split('\t')
    if len(data)!=2:
        continue
    key_in,value_in = data
    if prev_key and key_in != prev_key:
        print('{0}\t{1}'.format(prev_key,max_cost))
        max_cost = 0
    prev_key = key_in
    max_cost = max(max_cost,float(value_in))
