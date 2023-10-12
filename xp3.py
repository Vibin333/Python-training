import re
def datecheck(date):
    pattern=r'(0[1-9]|1[0-2])/\d{2}/\d{4}$'
    return bool(re.match(pattern,date))
date='01/25/2023'
if datecheck(date):
    print("Valid")
else:
    print("invalid")