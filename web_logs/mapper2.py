#!/usr/bin/env python
import sys
import re
pattern = re.compile(r'^([0-9.]+)\s([\w.-]+)\s([\w.-]+)\s(\[[^\[\]]+\])\s"((?:[^"]|\")+)"\s(\d{3})\s(\d+|-)$')
for line in sys.stdin:
    result = pattern.match(line)
    if not result:
        continue
    else:
        ip_info = result.group(1)
        if ip_info:
            print '{0}\t{1}'.format(ip_info,1)
