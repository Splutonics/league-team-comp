from distutils import command
from gc import callbacks
from tkinter import *
from tkinter import ttk
from lookup_summoner import *

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Label(frm, text="Summoner "+"1").grid(column=0, row=1)
s1 = ttk.Entry(frm)
s1.grid(column=1, row=1)

ttk.Label(frm, text="Min Level").grid(column=2, row=0)
s1_l = ttk.Entry(frm)
s1_l.grid(column=2, row=1)

ttk.Button(frm,
           text="Get Champions",
           command=lambda: lookup_summoner(s1.get(), int(s1_l.get()))
           ).grid(column=0, row=3)

ttk.Button(frm, text="Quit", command=root.destroy).grid(column=12, row=12)
root.mainloop()
