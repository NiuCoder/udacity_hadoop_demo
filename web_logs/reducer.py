#!/usr/bin/env python
import sys
total_hits = 0
prev_path = ' '
line_cnt = 0
for line in sys.stdin:
    line_cnt += 1
    path,count = line.split('\t')
    if path != prev_path:
        if line_cnt>1:
            print '{0}\t{1}'.format(prev_path,total_hits)
            total_hits = 0
    prev_path = path
    total_hits += int(count)
print '{0}\t{1}'.format(prev_path,total_hits)
