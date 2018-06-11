#!/usr/bin/env python
import sys
import re
for line in sys.stdin:
    data = line.split('\t')
    if len(data)!=19:
        continue
    if not data[0].isdigit():
        continue
    author_id = data[3]
    added_at = data[8]
    if not author_id or not added_at:
        continue
    pattern = re.compile(r"\d{4}-\d{2}-\d{2}\s(\d{2}):\d{2}:\d{2}.\d+\+\d+")
    result = pattern.match(added_at)
    if not result:
        continue
    hour = result.group(1)
    print '{0}\t{1}\t{2}'.format(author_id,hour,1)
