#This section of the catalog is for a technology department. Options are included for adding and searching entries in the catalog.

#Harrison Birkner
#5/7/2020

import json
import tkinter as tk
import tkinter.messagebox

class techDept:
    #init sets up the main window
    def __init__(self):
        #Setting up a dictionary with some predefined options
        self.techItems = {'iPhone X': 1000.00, 'Samsung Galaxy S10': 1000.00, 'Moto G7': 200.00, 'Moto G Stylus': 300.00}
        
		#This section was written by Ben or Gabe, not Harrison
		with open('techinventory.txt', 'w') as f:
            json.dump(self.techItems, f)
		######################################################
		
        #creating the main window
        self.wdwTech = tk.Tk()

        #creating and packing the textbox for entry
        self.txbTechItem = tk.Entry()
        self.txbTechItem.pack()

        #creating and packing the 3 main buttons for searching for items, adding items, and quiting the program
        self.btnSearch = tk.Button(self.wdwTech, text = 'Search', command = self.search)
        self.btnSearch.pack(side = 'left')
        self.btnAddWdw = tk.Button(self.wdwTech, text = 'Add Item', command = self.add)
        self.btnAddWdw.pack(side = 'left')
        self.btnQuit = tk.Button(self.wdwTech, text = 'Quit', command = self.wdwTech.destroy)
        self.btnQuit.pack(side = 'left')

        #start the window loop
        tk.mainloop()

    #search creates the window for search results
    def search(self):
        #data from the main windows textbox is grabbed and moved into a variable
        self.itemInput = self.txbTechItem.get()

        #the search window is created
        self.wdwSearch = tk.Tk()

        #Button the close the search window is created and packed. The command closes the windows and clears the textbox of the main window
        self.btnSearchQuit = tk.Button(self.wdwSearch, text = "Go Back", command = lambda:[self.txbTechItem.delete(0, 'end'), self.wdwSearch.destroy()])
        self.btnSearchQuit.pack()

        #if the item is found in the list...
        if self.itemInput in self.techItems:
            #the price associated with the item is found, moved to a variable,
            #and a message is printed with the info. Otherwise...
            self.price = str(self.techItems[self.itemInput])
            self.lblSrchRslt = tk.Label(self.wdwSearch, text = self.itemInput + '\nPrice: $' + self.price)
            self.lblSrchRslt.pack()
        else:
            #A message is printed informing the user the item does not exist in the system
            self.lblSrchRslt = tk.Label(self.wdwSearch, text = 'Oops! ' + self.itemInput + ' does not exist in the system.')
            self.lblSrchRslt.pack()
       
        #start the windows main loop
        tk.mainloop()

    #add opens a windows for adding an entry to the technology catalog (dictionary)
    def add(self):
        #the add window is created
        self.wdwAdd = tk.Tk()

        #two frames are created and packed for positioning
        self.framelbl = tk.Frame(self.wdwAdd)
        self.framelbl.pack(side = 'left')
        self.frameEntry = tk.Frame(self.wdwAdd)
        self.frameEntry.pack(side = 'left')

        #data from the main windows textbox is grabbed and moved into a variable
        self.itemInput = self.txbTechItem.get()

        #a textbox for the new item is created and packed
        self.txbNewItem = tk.Entry(self.frameEntry)
        self.txbNewItem.pack()

        #the item from the main window's textbox is moved into the new item textbox
        self.txbNewItem.insert(0, self.itemInput)

        #a textbox for the new item's price is created and packed
        self.txbNewPrice = tk.Entry(self.frameEntry)
        self.txbNewPrice.pack()
       
        #labels are created and packed for the corresponding textboxes
        self.lblPhone = tk.Label(self.framelbl, text = "Enter device name:")
        self.lblPhone.pack()
        self.lblPrice = tk.Label(self.framelbl, text = "Enter price:")
        self.lblPrice.pack()

        #a button is created and packed for adding the item
        self.btnAdd = tk.Button(self.wdwAdd, text = "Add Item", command = self.verifyAdd)
        self.btnAdd.pack(side = 'right')

        #start the windows main loop
        tk.mainloop()
   
    #verifyAdd verifies the information entered from the add window
    def verifyAdd(self):
        #the new item and price are moved into variables
        self.itemInput = self.txbNewItem.get()
        self.priceInput = self.txbNewPrice.get()

        #if the item is blank...
        if self.itemInput == '':
            #an error is printed and the user is returned to the add item window. Otherwise...
            tk.messagebox.showinfo('Error', 'Item field required.')
            return
        #if the price is blank...
        elif self.priceInput == '':
            #an error is printed and the user is returned to the add item window. Otherwise...
            tk.messagebox.showinfo('Error', 'Price field required.')
            return
        #if the price is not a number...
        elif not self.priceInput.isdigit():
            #an error is printed and the user is returned to the add item window. Otherwise...
            tk.messagebox.showinfo('Error', 'Price must be number.')
            return

        #the price is converted to a number
        self.priceInput = float(self.priceInput)
        #a new entry is created in the catalog(dictionary) for the item
        self.techItems[self.itemInput] = self.priceInput
        #the add window is closed
        self.wdwAdd.destroy()
        #a message is printed informing the user the item was added successfully.
        tk.messagebox.showinfo('', 'Item added to catalog.')

#a new instance of the class techDept is created
myTechDept = techDept()