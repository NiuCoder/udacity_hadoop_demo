#!/usr/bin/env python
import sys
num_sales=0
total_cost=0
for line in sys.stdin:
    data = line.strip().split('\t')
    if len(data)!=2:
        continue
    store,cost = data
    num_sales +=1
    total_cost += float(cost)
print('num_sales:{0}\ttotal_cost:{1}'.format(num_sales,total_cost))
