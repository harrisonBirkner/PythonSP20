#My section of the project is a sporting department in a store that allows user to search through items in the department.
#By Ben Oliver

import json
import tkinter as tk
import tkinter.messagebox

def init():
    #creating and naming the window
    windowBaseball = tk.Tk()
    windowBaseball.title('Baseball Department')
    
    Item = tk.Entry()
    Item.pack()

    #search button must use lambda if passing an argument
    btnSearch = tk.Button(windowBaseball, text = 'Search', command = lambda:inventory(Item))
    btnSearch.pack(side = 'left')
    btnQuit = tk.Button(windowBaseball, text = 'Quit', command = windowBaseball.destroy)
    btnQuit.pack(side = 'right')

    tk.mainloop()

def inventory(Item):

    #Dictionary with items in the store
    baseballCatalog = {'Louisville Slugger': 500.00, 'Nike Force Cleats': 60.00, 'Rawlings Batting Gloves': 18.00, 'Nike Glasses': 36.00}
    with open('baseballinventory.txt', 'w') as f:
        json.dump(baseballCatalog, f)
    
    input = Item.get()
    windowSearch = tk.Tk()
    btnSearchQuit = tk.Button(windowSearch, text = "Go Back", command = lambda:[Item.delete(0, 'end'), windowSearch.destroy()])
    btnSearchQuit.pack()

    #If statement to check the dictionary for matching item
    if input in baseballCatalog:
        cost = str(baseballCatalog[input])
        info = tk.Label(windowSearch, text = input + '\nCost: $' + cost)
        info.pack()
    else:
        info = tk.Label(windowSearch, text = 'Error' + input + ' cannot be found.')
        info.pack()


init()