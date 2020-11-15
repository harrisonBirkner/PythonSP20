# This program displays a label with text

import tkinter

class MyGUI:
    def __init__(self):
        #Create the main window widget
        self.main_window = tkinter.Tk()

        #Create a label widget containing text
        self.label1 = tkinter.Label(self.main_window, text = "Isn't this wonderful!")
        self.label2 = tkinter.Label(self.main_window, text = "You have to be impressed now.")

        #Call the Label widget's pack method
        self.label1.pack(side='left')
        self.label2.pack(side = 'left')
        # Enter the tkinter main loop
        tkinter.mainloop()

#Create an instance of the MyGUI class
my_gui = MyGUI()



