#Gabriel did the menu yes the gabriel yall all love :) <3
from tkinter import *
import tkinter as tk
import json
jeff = tk.Tk()

def Tech():
    import Harrison
def Base():
    import Ben
def Output():
   base = open("baseballinventory.txt", "r").read()
   tech = open("techinventory.txt","r").read()
   print(base, "\n", tech)

Yeet = tk.Frame(jeff)
Yeet.pack()

tech = tk.Button(Yeet, text='Technology',command=Tech)
tech.pack()

base = tk.Button(Yeet, text='BaseBall',command=Base)
base.pack()

prt = tk.Button(Yeet, text = 'Print the List of items in iventory',command=Output)
prt.pack()

exit = tk.Button(Yeet, text='Exit',command=jeff.destroy)
exit.pack()



jeff.mainloop()
