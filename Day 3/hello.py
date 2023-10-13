import tkinter as tk
window=tk.Tk()
window.title("Hello")
window.configure(bg='#181818')
window.geometry('300x280')
lab1=tk.Label(window,text='Hello World',font='Inter',bg='#181818',fg='#c0c0c0')
lab1.grid(row=1,column=1,padx=10,pady=10)