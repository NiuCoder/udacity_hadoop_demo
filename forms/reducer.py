#!/usr/bin/env python
import sys
prev_author_id = None
prev_hour = None
line_cnt = 0
total_hour_cnt = 0
max_cnt_hour = []
max_hour_cnt = 0
for line in sys.stdin:
    data = line.split('\t')
    if len(data)!=3:
        continue
    line_cnt += 1
    author_id,hour,count = data
    if author_id!=prev_author_id:
         if line_cnt>1:
            if max_hour_cnt == 0:
                max_cnt_hour.append(prev_hour)
            for h in max_cnt_hour:    
                print '{0}\t{1}'.format(prev_author_id,h)
            max_cnt_hour = []
            max_hour_cnt = 0
            prev_hour = None
            total_hour_cnt = 0
    prev_author_id = author_id
    if hour!=prev_hour and prev_hour:
        total_hour_cnt = int(count)
    else:
        total_hour_cnt += int(count)

    if total_hour_cnt>max_hour_cnt:
        max_hour_cnt = total_hour_cnt
        max_cnt_hour = []
        max_cnt_hour.append(hour)
    elif total_hour_cnt==max_hour_cnt:
        max_cnt_hour.append(hour)
    prev_hour = hour
for h in max_cnt_hour:
    print '{0}\t{1}'.format(prev_author_id,h)
        
