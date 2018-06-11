#!/usr/bin/env python
import sys
import re
pattern = re.compile(r'^([0-9.]+)\s([\w.-]+)\s([\w.-]+)\s(\[[^\[\]]+\])\s"((?:[^"]|\")+)"\s(\d{3})\s(\d+|-)$')
for line in sys.stdin:
    result = pattern.match(line)
    if not result:
        continue
    else:
        request_info = result.group(5)
        data = request_info.split(' ')
        if len(data)!=3:
            continue
        mothod,path,protocol = data
        pattern2 = re.compile(r"(^.*https?://[^\/]+)?(/[^$]+)$")
        filepath = pattern2.match(path)
        if not filepath:
            continue
        filepath = filepath.group(2)
        print '{0}\t{1}'.format(filepath,1)
