#This program asks for the price of 5 items, and then displays a receipt listing the price of all 5 items, 
#subtotal of the sales, the amount of the sales tax, and the total.  

#The following 5 statements display input asking for the price of 5 items
item1 = float(input("Please enter the price of your first item "))
item2 = float(input("Please enter the price of your second item "))
item3 = float(input("Please enter the price of your third item "))
item4 = float(input("Please enter the price of your fourth item "))
item5 = float(input("Please enter the price of your fifth item "))

#These 3 statements calculate the subtotal, sales tax, and total
subtotal = item1 + item2 + item3 + item4 + item5
salesTax = subtotal * 0.07
total = subtotal + salesTax

#The next 6 statements print labels for the receipt and items and formatted amounts
print('\n**********RECIEPT**********\n')
print('first item\t'+'$'+format(item1,'10,.2f'))
print('second item\t'+'$'+format(item2,'10,.2f'))
print('third item\t'+'$'+format(item3,'10,.2f'))
print('fourth item\t'+'$'+format(item4,'10,.2f'))
print('fifth item\t'+'$'+format(item5,'10,.2f'))

#The following 3 statements print labels for totals and the formatted amounts
print('\nSubtotal\t'+'$'+format(subtotal,'10,.2f'))
print('Sales Tax\t'+'$'+format(salesTax,'10,.2f'))
print('Total\t\t'+'$'+format(total,'10,.2f'))
