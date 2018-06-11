#!/usr/bin/env python
import sys
total_cost = 0
prev_key = None
for line in sys.stdin:
    data = line.strip().split('\t')
    if len(data)!=2:
        continue
    key_in,value_in = data
    if key_in != prev_key and prev_key:
        print('{0}\t{1}'.format(prev_key,total_cost))
        total_cost = 0
    prev_key = key_in
    total_cost += float(value_in)
