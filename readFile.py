#This program displays the records in
#the coffee.dat file

#Harrison Birkner
#3/27/20

coffeeFile = open('coffee.dat', 'r')

def main():
	desc = inputValues()
	while desc != '':
		qty = float(inputValues())
		
		#strip the \n from description
		desc = desc.rstrip('\n')
		
		output(qty, desc)
		
		desc = inputValues()
	coffeeFile.close()
	
def inputValues():
	iData = coffeeFile.readline()
	return iData
	
def output(qty, desc):
	print("Description", desc)
	print("Quantity:", qty)
	
main()