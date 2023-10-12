import re
def numcheck(num):
    pattern=r'-?\d+\.?'
    number=re.findall(pattern,num)
    print(number)
sentence='hai yo 807'
numcheck(sentence)