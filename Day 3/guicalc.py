import tkinter as tk

def add():
    num1=int(ent1.get())
    num2=int(ent2.get())
    sum=num1+num2
    lab3.config(text=str(sum))

def sub():
    num1=int(ent1.get())
    num2=int(ent2.get())
    diff=num1-num2
    lab3.config(text=str(diff))
    
def mult():
    num1=int(ent1.get())
    num2=int(ent2.get())
    prod=num1*num2
    lab3.config(text=str(prod))
    
def div():
    num1=int(ent1.get())
    num2=int(ent2.get())
    q=num1+num2
    lab3.config(text=str(q))
    
window=tk.Tk()
window.title("Hello")
window.configure(bg='#181818')
window.geometry('600x280')
lab1=tk.Label(window,text='Calculator',font='Inter',bg='#181818',fg='#c0c0c0')
lab1.grid(row=1,column=1,padx=100,pady=10)
lab2=tk.Label(window,text='Enter number 1:',font='Inter',bg='#181818',fg='#c0c0c0')
lab2.grid(row=2,column=1,padx=100,pady=10)
lab3=tk.Label(window,text='Enter number 2:',font='Inter',bg='#181818',fg='#c0c0c0')
lab3.grid(row=3,column=1,padx=100,pady=10)
ent1=tk.Entry(window)
ent1.grid(row=2,column=2,padx=10,pady=10)
ent2=tk.Entry(window)
ent2.grid(row=3,column=2,padx=10,pady=10)
but1=tk.Button(window,text='+',bg='#181818',fg='#c0c0c0',command=add)
but1.grid(row=4,column=1,padx=10,pady=10)
but2=tk.Button(window,text='-',bg='#181818',fg='#c0c0c0',command=sub)
but2.grid(row=4,column=2,padx=10,pady=10)
but3=tk.Button(window,text='*',bg='#181818',fg='#c0c0c0',command=mult)
but3.grid(row=4,column=3,padx=10,pady=10)
but4=tk.Button(window,text='/',bg='#181818',fg='#c0c0c0',command=div)
but4.grid(row=4,column=4,padx=10,pady=10)
lab3=tk.Label(window,text='Result',font='Inter',bg='#181818',fg='#c0c0c0')
lab3.grid(row=5,column=1,padx=100,pady=10)
window.mainloop()