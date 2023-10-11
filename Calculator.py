def add(n1,n2):
    print(n1+n2)
    
def sub(n1,n2):
    print(n1-n2)
    
def mult(n1,n2):
    print(n1*n2)
    
def div(n1,n2):
    print(n1/n2)
    
def exp(n1,n2):
    print(n1**n2)
    
def rem(n1,n2):
    print(n1%n2)
    
def cal():
    y=True
    while(y==True):
        number1=int(input("Enter number 1: "))
        number2=int(input("Enter number 2: "))
        choice=(input("Enter choice (+,-,*,/,^,%): "))
        if(choice=='+'):
            add(number1,number2)
        elif(choice=='-'):
            sub(number1,number2)
        elif(choice=='*'):
            mult(number1,number2)
        elif(choice=='/'):
            div(number1,number2)
        elif(choice=='^'):
            exp(number1,number2)
        elif(choice=='%'):
            rem(number1,number2)
        else:
            print("Choice error")
        exit=input("Want to continue?(y/n)")
        if exit == 'y':
            y=True
        elif exit =='n':
            y=False
        else:
            print("Wrong option")
cal()