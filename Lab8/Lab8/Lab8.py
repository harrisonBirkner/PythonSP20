#This program displays checkboxes for various services at a mechanic's shop. It displays a total cost for services selected.

#Harrison Birkner
#4/30/2020

import tkinter
import tkinter.messagebox

class repairCostPrgm:
    def __init__(self):
        #Create the main window widget
        self.main_window = tkinter.Tk()

        #Create two frames. One for the Checkbuttons and another for the regular Button widgets.
        self.cb_frame = tkinter.Frame(self.main_window)
        self.btn_frame = tkinter.Frame(self.main_window)

        #Create the IntVar objects to use with the Checkbuttons
        self.cbOilVar = tkinter.IntVar()
        self.cbLubeVar = tkinter.IntVar()
        self.cbRadVar = tkinter.IntVar()
        self.cbTranVar = tkinter.IntVar()
        self.cbInspVar = tkinter.IntVar()
        self.cbMuffVar = tkinter.IntVar()
        self.cbTireVar = tkinter.IntVar()

        #Set the intVar objects to 0
        self.cbOilVar.set(0)
        self.cbLubeVar.set(0)
        self.cbRadVar.set(0)
        self.cbTranVar.set(0)
        self.cbInspVar.set(0)
        self.cbMuffVar.set(0)
        self.cbTireVar.set(0)

        #Create the Checkbutton widgets in the cb_frame
        self.cbOil = tkinter.Checkbutton(self.cb_frame, text = 'Oil change', variable=self.cbOilVar)
        self.cbLube = tkinter.Checkbutton(self.cb_frame, text = 'Lube job', variable=self.cbLubeVar)
        self.cbRad = tkinter.Checkbutton(self.cb_frame, text = 'Radiator flush', variable=self.cbRadVar)
        self.cbTran = tkinter.Checkbutton(self.cb_frame, text = 'Transmission flush', variable = self.cbTranVar)
        self.cbInsp = tkinter.Checkbutton(self.cb_frame, text = 'Inspection', variable = self.cbInspVar)
        self.cbMuff = tkinter.Checkbutton(self.cb_frame, text = 'Muffler replacement', variable = self.cbMuffVar)
        self.cbTire = tkinter.Checkbutton(self.cb_frame, text = 'Tire rotation', variable = self.cbTireVar)

        #Pack the Checkbuttons
        self.cbOil.pack()
        self.cbLube.pack()
        self.cbRad.pack()
        self.cbTran.pack()
        self.cbInsp.pack()
        self.cbMuff.pack()
        self.cbTire.pack()

        #Create the Button widgets.
        #The calcCost method should be executed when the user clicks the "Calculate Total Cost" button.
        #The program is closed when the user clicks the "Quit" button.
        self.btnCost = tkinter.Button(self.btn_frame, text = 'Calculate Total Cost', command = self.calcCost)
        self.btnQuit = tkinter.Button(self.btn_frame, text = 'Quit', command = self.main_window.destroy) 
        
        #Pack the Buttons
        self.btnCost.pack(side = 'left')
        self.btnQuit.pack(side = 'left')

        #Pack the frames
        self.cb_frame.pack()
        self.btn_frame.pack()

        #Enter the tkinter main loop
        tkinter.mainloop()

    #The calcCost method is a callback function for the Button widget
    def calcCost(self):
        self.cost = 0

        #If a checkbox is checked an amount is added to the cost variable
        if self.cbOilVar.get() == 1:
            self.cost += 30
        if self.cbLubeVar.get() == 1:
            self.cost += 20
        if self.cbRadVar.get() == 1:
            self.cost += 40
        if self.cbTranVar.get() == 1:
            self.cost += 100
        if self.cbInspVar.get() == 1:
            self.cost += 35
        if self.cbMuffVar.get() == 1:
            self.cost += 200
        if self.cbTireVar.get() == 1:
            self.cost += 20

        #Display an info dialog box with formatted cost
        tkinter.messagebox.showinfo('Total Cost', 'Your total cost is: $' + str(self.cost))

#Create an instance of the repairCostPrgm class
my_prgm = repairCostPrgm()
