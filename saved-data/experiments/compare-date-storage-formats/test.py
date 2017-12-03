#!/usr/bin/env python3.4

created_at = "2012-07-20T01:19:13Z"

import sys
print("Size as string:", sys.getsizeof(created_at))

# Install with "pip-3.4 install python-dateutil"
import dateutil.parser
datetime_created_at = dateutil.parser.parse(created_at)
print("Size as datetime object:", sys.getsizeof(datetime_created_at))

tuple_created_at = datetime_created_at.timetuple()
print("Size as time tuple:", sys.getsizeof(tuple_created_at))

import time
timestamp_created_at = time.mktime(datetime_created_at.timetuple())
print("Size as POSIX time stamp float:", sys.getsizeof(timestamp_created_at))

# See explanation here: http://stackoverflow.com/a/8778548/743730
import calendar
print("Size of timegm integer:", sys.getsizeof(calendar.timegm(tuple_created_at)))
