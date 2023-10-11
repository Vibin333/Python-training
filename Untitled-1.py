#1
print(int(3+float('3.0')))
#2
a=3
A=4
print(a+3+7)

#3
print(3+True)

#4
"""name=input("Enter ur name: ")
age=int(input("Enter ur age: "))
if(name=='Vibin'):
    print('My name is',name,'and age is',age)
else:
    print("Invalid name")"""

#6
"""name1=input("Enter ur name: ")
name2=input("Enter ur name: ")
age1=int(input("Enter ur age: "))
age2=int(input("Enter ur age: "))
if age1>age2:
    print('My name is',name1,'and age is',age1)
else:
    print('My name is',name2,'and age is',age2)"""

#7
"""def collect1():
    name=input("Enter ur name: ")
    age=int(input("Enter ur age: "))
    print('My name is',name,'and age is',age)
collect1()

def collect2():
    name=input("Enter ur name: ")
    age=int(input("Enter ur age: "))
    if(name=="Vibin"):
        print('My name is',name,'and age is',age)
    else:
        print("name error")
collect2()

def collect3():
    name1=input("Enter ur name: ")
    name2=input("Enter ur name: ")
    age1=int(input("Enter ur age: "))
    age2=int(input("Enter ur age: "))
    if age1>age2:
        print('My name is',name1,'and age is',age1)
    else:
        print('My name is',name2,'and age is',age2)
collect3()"""

#8
def add(n1,n2):
    print(n1+n2)
def sub(n1,n2):
    print(n1-n2)
def mult(n1,n2):
    print(n1*n2)
def div(n1,n2):
    print(n1/n2)
number1=int(input("Enter number 1: "))
number2=int(input("Enter number 2: "))
choice=(int(input("Enter choice from 1 to 4(1 to add 2 to sub 3 to mult 4 to div): ")))
if(choice==1):
    add(number1,number2)
elif(choice==2):
    sub(number1,number2)
elif(choice==3):
    mult(number1,number2)
elif(choice==4):
    div(number1,number2)
else:
    print("Choice error")