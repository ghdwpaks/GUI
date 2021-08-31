import tkinter as t
from tkinter.constants import INSERT



w = t.Tk()
w.title("hello")
w.geometry("640x480+100+100")
w.resizable(False, False)

lb = t.Listbox(w,selectmode="extended",height=0)
inserts = "0"+"1"+"2"
lb.insert(0,inserts)
lb.insert(0,"02")
lb.insert(0,"03")
lb.insert(1,"11")
lb.insert(2,"22")
lb.insert(3,"33")
lb.pack()


w.mainloop()
