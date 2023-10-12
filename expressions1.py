import re
def mailcheck(mail):
    pattern='\w*@\w*.\w{3}$'
    return bool(re.match(pattern,mail))
mail='sunny@gmail.com'
if mailcheck(mail):
    print("Valid")
else:
    print("invalid")