import re
def passcheck(passw):
    pattern='(?=.*[A-Z])(?=.*\d).{8,}'
    return bool(re.match(pattern,passw))
passw='Aa123232'
if passcheck(passw):
    print("Valid")
else:
    print("invalid")