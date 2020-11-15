#This program adds golfer's names and scores
#to the golf.dat file

#Harrison Birkner
#3/27/20

#this try/except clause checks for errors opening the dat file
try:
	golfFile = open('golf.dat', 'a')
except IOError:
	print("ERROR! There was an issue opening the file 'golf.dat'.")

#userInput asks the user for the various input data	
def userInput():
	print("Enter the following golf data:") 
	#This while loop continues until valid data has been entered
	while True:
		#this try/except clause checks that the score input is numeric data
		try:
			name = input("Golfer's name: ")
			score = int(input("Score: "))
			break
		except ValueError:
			print('ERROR! Score must be numeric.')

	return name, score

#output prints the input data to golf.dat
def output(name, score):
	golfFile.write(name + '\n')
	golfFile.write(str(score) + '\n')
	
#main controls the overall loop and structure of the program.
def main():
	playAgain = 'Y'
	while playAgain == 'Y':
		name, score = userInput()
		output(name, score)
		
		print('Do you want to add another record?')
		#This input automatically converts playAgain to uppercase
		#for easier comparison at the beginning of the loop.
		playAgain = input('y = yes, anything else = no ').upper()
	#This closes the output file and notifies the user the program is finished running
	golfFile.close()
	print("Program Ended")
	
main()
