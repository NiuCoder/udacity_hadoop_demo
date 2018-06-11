#!/usr/bin/env python
import sys
total_hits = 0
prev_ip = ' '
line_cnt = 0
for line in sys.stdin:
    line_cnt += 1
    ip,count = line.split('\t')
    if ip != prev_ip:
        if line_cnt>1:
            print '{0}\t{1}'.format(prev_ip,total_hits)
            total_hits = 0
    prev_ip = ip
    total_hits += int(count)
print '{0}\t{1}'.format(prev_ip,total_hits)
