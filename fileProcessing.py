#This program adds coffe inventory records
#to the coffee.dat file

#Harrison Birkner
#3/27/20

coffeeFile = open('coffee.dat', 'w')

def init():
	#opening file from inside program directory:
	# open modes:
	#
	#r for read
	#
	#w for writing output
	#
	#a to append on end
	coffeeFile = open('coffee.dat', 'w')
	
	#opening file from a different location:
	#this 'r' doesn't mean read, it is telling
	#the program the file is in a seperate directory
	# coffeFile = open(r'C:\python\coffee.dat', 'w')

def userInput():
	print("Enter the following coffee data:") 
	desc = input("Description: ")
	qty = int(input("Quantity (in pounds): "))
	
	return desc, qty
	
def output(desc, qty):
	coffeeFile.write(desc + '\n')
	coffeeFile.write(str(qty) + '\n')
	
def main():
	#init()
	playAgain = 'y'
	while playAgain == 'y' or playAgain == 'Y':
		desc, qty = userInput()
		output(desc, qty)
		
		print('Do you want to add another record?')
		playAgain = input('y = yes, anything else = no')
	coffeeFile.close()
	print("Program Ended")
	
main()