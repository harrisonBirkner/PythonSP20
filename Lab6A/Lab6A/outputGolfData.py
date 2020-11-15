#This program uses the golf.dat file as input
#and returns a formatted list of golfer's names and their scores
#as well as a leaderboard of the first and second place winners

#Harrison Birkner
#3/27/20

import math

#this try/except clause checks for errors opening the dat file
try:
	golfFile = open('golf.dat', 'r')
except IOError:
	print("ERROR! There was an issue opening the file 'golf.dat'.")

#main controls the overall loop and structure of the program
def main():
	#here counters and accumulators are set up
	#as well as placeholders for first and second place
	totalScore = 0
	firstScore = 9999999999
	secScore = 9999999999
	numScores = 0
	
	#inputValues is called and data is returned into the name variable
	name = inputValues()
	
	#headers are printed
	print('Golfer\t\t\t      | Score')
	print('------------------------------|------')

	#strip the \n from name
	name = name.rstrip('\n')

	#this while loop runs while there are still lines of data
	#to be read from the input file
	while name != '':
		
		#inputValues is called and data is returned into the score variable
		score = int(inputValues())
		
		#this if structure checks if the new score
		#is smaller than the current first place score,
		#and if not it checks it against the current
		#second place score
		if score < firstScore:
			firstName = name
			firstScore = score
		elif score < secScore:
			secName = name
			secScore = score
	
		#The current score is added to an accumulator
		#and 1 is added to a score counter, both for 
		#a future calculation
		totalScore += score
		numScores +=1
		
		output(score, name)
	
		name = inputValues()

		#strips the \n from name
		name = name.rstrip('\n')
	
	#The average score is calculated, using the accumulated
	#total score and the score counter variables
	avgScore = totalScore / numScores

	totalsClosing(avgScore, firstName, firstScore, secName, secScore)

#inputValues reads a line from golf.dat, moves it into iData, and returns it	
def inputValues():
	iData = golfFile.readline()
	return iData

#output takes 2 arguments and formats and prints data passed into it	
def output(score, name):
	print(format(name, '30') + '|\t' + format(score, '5,'))

#totalsClosing prints the average score and the leaderboards
def totalsClosing(avgScore, firstName, firstScore, secName, secScore):
	print('\nThe average score was', format(math.trunc(avgScore), ',') + '!\n')
	print('**********LEADERBOARD**********')
	print('             ____')
	print('            /    |')
	print('           /_/|  |')
	print('              |  |')
	print('              |  |')
	print('              |  |')
	print('              |  |')
	print('              |  |')
	print('           ___|  |___')
	print('          |__________|ST PLACE GOES TO...\n')
	print(firstName, 'with', firstScore, 'points!\n')
	print('            _________ ')
	print('           |_________|')
	print('                   | |')
	print('           ________| |')
	print('           |  _______|')
	print('           | |')
	print('           | |_______')
	print('           |_________|ND PLACE GOES TO...\n')
	print(secName, 'with', secScore, 'points!')
	golfFile.close()
	
main()
