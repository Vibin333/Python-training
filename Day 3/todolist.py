import tkinter as tk
import tkmacosx as tkm
from tkinter import font

def enter():
    task=ent1.get()
    if(task):
        lbox1.insert(tk.END,task)
        ent1.delete(0,tk.END)

def remove():
    taskindex=lbox1.curselection()
    for index in taskindex:
        lbox1.delete(index)
    
def green():
    taskindex=lbox1.curselection()
    lbox1.itemconfig(taskindex,{'bg':'#71c562'})

def clear():
    lbox1.delete(0,tk.END)
    
window=tk.Tk()
window.geometry('590x320')
window.title("To Do List")
window.config(bg='#181d1d')
lab1=tk.Label(window,text='Enter task:',bg='#181d1d',fg='#e4f8f7',font=('cormorant garamond',20))
lab1.grid(row=1,column=1)
ent1=tk.Entry(window,borderwidth=0,font=8,bg='#233030',fg='#f2f2f2')
ent1.grid(row=1,column=2)
but1=tkm.Button(window,text='Add',bg='#4eded7',fg='#f2f2f2',height=30,width=60,borderless=1,font=29,command=enter)
but1.grid(row=1,column=3,padx=30,pady=20)
lbox1=tk.Listbox(window,bg='#233030',fg='#f2f2f2',width=45,height=7,font=('Noto Sans',15),borderwidth=0)
lbox1.grid(row=2,column=1,columnspan=15)
but2=tkm.Button(window,text='Remove',bg='#f93555',fg='#f2f2f2',font=29,borderless=1,command=remove)
but2.grid(row=3,column=1,padx=30,pady=20)
but3=tkm.Button(window,text='Completed',bg='#71c562',fg='#f2f2f2',font=29,borderless=1,command=green)
but3.grid(row=3,column=2,padx=30,pady=20)
but4=tkm.Button(window,text='Clear',bg='#4eded7',fg='#f2f2f2',font=29,borderless=1,command=clear)
but4.grid(row=3,column=3,padx=30,pady=20)
window.mainloop()