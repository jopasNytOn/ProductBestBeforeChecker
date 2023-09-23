#!/usr/bin/env python

import datetime
import re
import sys

def convert_product_date_to_real_date(product_date):
    match = re.search('(\d*)[\.\/\-](\d*)[\.\/\-](\d*)', product_date)
    if match:
        if int(match.group(3)) < 2000:
            return True, datetime.date(2000 + int(match.group(3)), int(match.group(2)), int(match.group(1)))
        else:
            return True, datetime.date(int(match.group(3)), int(match.group(2)), int(match.group(1)))
    match = re.search('(\d*)[\-](\d*)', product_date)
    if match:
        return True, datetime.date(int(match.group(2)), int(match.group(1)), 15)
    return False, product_date

today = datetime.date.today()
print("v0.3\n\nToday", today, "\n")

if len(sys.argv) == 2:
    csv_lines = open(sys.argv[1], 'r').read().split('\n')
    for line in csv_lines:
        match = re.search('(.*); (.*); (.*)', line)
        if match:
            success, product_date = convert_product_date_to_real_date(match.group(3))
            if success:
                valid = product_date - today > datetime.timedelta(days=30)
                if not valid:
                    print(match.group(1), product_date)
