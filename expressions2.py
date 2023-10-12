import re
def numcheck(num):
    pattern=r'\(\d{3}\) \d{3}-\d{3}$'
    return bool(re.match(pattern,num))
num='(555) 555-555'
if numcheck(num):
    print("Valid")
else:
    print("invalid")