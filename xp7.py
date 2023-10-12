import re
def tagcheck(tag):
    pattern='#\w+'
    return bool(re.match(pattern,tag))
tag='#Aa123232'
if tagcheck(tag):
    print("Valid")
else:
    print("invalid")