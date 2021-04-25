from tkinter import *
from tkinter.ttk import *
from time import strftime

root=Tk()
root.title('DClock-001')
root.resizable(False,False)
root.iconbitmap('icon.ico')

def time():
	string=strftime('%H:%M:%S %p')
	label.config(text=string)
	label.after(1000,time)

label=Label(root,font=("ds-digital",80),background='black',foreground="cyan")
label.pack(anchor='center')
time()

mainloop()