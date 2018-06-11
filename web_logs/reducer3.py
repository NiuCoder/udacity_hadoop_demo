#!/usr/bin/env python
import sys
total_hits = 0
prev_path = ' '
line_cnt = 0
max_occur_path = ' '
max_occur_time = 0
for line in sys.stdin:
    line_cnt += 1
    path,count = line.split('\t')
    if path != prev_path:
        if line_cnt>1:
            if total_hits > max_occur_time:
                max_occur_time = total_hits
                max_occur_path = prev_path
            total_hits = 0
    prev_path = path
    total_hits += int(count)
if total_hits>max_occur_time:
    max_occur_time = total_hits
    max_occur_path = prev_path
print '{0}\t{1}'.format(max_occur_path,max_occur_time)
