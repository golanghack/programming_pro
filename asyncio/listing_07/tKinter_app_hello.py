#! /usr/bin/env python3 


import tkinter
from tkinter import ttk 

window = tkinter.Tk()
window.title('Hello')
window.geometry('400x300')

def say_hello():
    print('hello')
    
hello_button = ttk.Button(window, text='Say hello', command=say_hello)
hello_button.pack()

window.mainloop()