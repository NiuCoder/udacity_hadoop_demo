#!/usr/bin/env python
import sys
for line in sys.stdin:
    line = line.strip()
    data = line.split('\t')
    date,time,store,category,cost,method = data
   # print('{0}\t{1}'.format(category,cost))
    print('{0}\t{1}'.format(store,cost))
