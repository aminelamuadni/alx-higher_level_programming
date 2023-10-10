#!/usr/bin/python3
"""
Module for parsing logs and computing metrics.
"""


import sys


status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
                    "404": 0, "405": 0, "500": 0}
total_size = 0
line_count = 0

try:
    for line in sys.stdin:
        split_line = line.split()
        if len(split_line) < 2:
            continue
        status = split_line[-2]
        file_size = int(split_line[-1])
        if status in status_codes:
            status_codes[status] += 1
        total_size += file_size
        line_count += 1

        if line_count % 10 == 0:
            print("File size: {}".format(total_size))
            for code, count in sorted(status_codes.items()):
                if count > 0:
                    print("{}: {}".format(code, count))

except KeyboardInterrupt:
    pass
finally:
    print("File size: {}".format(total_size))
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print("{}: {}".format(code, count))
