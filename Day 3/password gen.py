import tkinter as tk
import re
import random
users={}
def generate():
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
        'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
        'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    caps = [
        'A', 'B', 'C', 'D',
        'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
        'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password=[]
    value=random.randint(2,4)
    for letter in range(value):
        password+=random.choice(letters)
    for digit in range(value):
        password+=random.choice(numbers)
    for sym in range(value):
        password+=random.choice(symbols)
    for alp in range(value):
        password+=random.choice(caps)

    random.shuffle(password)
    final=''
    for alphabet in password:
        final+=alphabet
    #print(final)
    ent2.delete(0, tk.END)
    ent2.insert(0,final)
    
def checkpass():
    password=ent2.get()
    pattern=r'^(?=.*[A-Z])(?=.*\d)(?=.*[!#$%&()*+])[A-Za-z\d!#$%&()*+]{8,}$'
    flag=bool(re.match(pattern,password))
    if(flag):
        lab2.config(fg='#39FF14')
        lab1.config(fg='#39FF14')
        users.update({"username":ent1.get(),"password":password})
        print(users)
    else:
        lab3=tk.Label(window,text='Try again',font='Inter',bg='#181818',fg='red')
        lab3.grid(rows=7,columns=2)
        window.after(750, lab3.destroy)
        lab2.config(fg='#c0c0c0')
        lab1.config(fg='#c0c0c0')
def showhide():
    if ent2['show']=='':
        ent2.config(show='*')
        but2.config(text='Show password')
    else:
        ent2.config(show='')
        but2.config(text='Hide password')

window=tk.Tk()
window.title("Login")
window.configure(bg='#181818')
window.geometry('300x280')
lab1=tk.Label(window,text='Username',font='Inter',bg='#181818',fg='#c0c0c0')
lab1.grid(row=1,column=1,padx=10,pady=10)
ent1=tk.Entry(window,bd=2)
ent1.grid(row=1,column=2,pady=10)
lab2=tk.Label(window,text='Password',font='Inter',bg='#181818',fg='#c0c0c0')
lab2.grid(row=3,column=1,padx=10,pady=10)
ent2=tk.Entry(window,bd=2,show='*')
ent2.grid(row=3,column=2,padx=10,pady=10)
but1=tk.Button(window,text="Submit",font='Inter',bg='#181818',fg='#c0c0c0',command=checkpass)
but1.grid(row=5,column=1,padx=10,pady=10)
but2=tk.Button(window,text="Show password",bg='#181818',fg='#c0c0c0',command=showhide)
but2.grid(row=5,column=2,padx=10,pady=10)
but3=tk.Button(window,text="Generate password",bg='#181818',fg='#c0c0c0',command=generate)
but3.grid(row=6,column=2,padx=10,pady=10)
window.mainloop()