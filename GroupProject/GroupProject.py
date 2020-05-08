#This is my section of a group project. The program is made to mimic the backend of an online catalog,
#specifically a technology department. There are options to search for entries upon different criteria,
#change entries data, remove, or see more info depending on the selection.

#Harrison Birkner
#5/7/2020

import tkinter as tk
import tkinter.messagebox

class techDept:
    def __init__(self):

        self.techWindow = tk.Tk()

        self.txbTechItem = tk.Entry()
        self.txbTechItem.pack()
        
        self.btnSearch = tk.Button(self.techWindow, text = 'Search', command =searchWindow)

        self.btnQuit = tk.Button(self.techWindow, text = 'Quit', command = self.techWindow.destroy)
        self.btnQuit.pack()
       
        tk.mainloop()
    
    def searchWindow():
        pass

myTechDept = techDept()