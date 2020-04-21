
#This program grades driver's license exams. It uses examAnswers.dat
#as input and compares the input answers to a hard coded list of correct answers,
#returning whether or not you passed, the number of correct answers, incorrect
#answers and a list of the questions incorrectly answered.

#Harrison Birkner
#4/17/2020

#init handles one time operations done at the beginning of the program
def init():
	#this try/except clause checks for errors opening the dat file
	try:
		examAnswers = open('examAnswers.dat', 'r')
	except IOError:
		print("ERROR! There was an issue opening the file 'examAnswers.dat'.")
	
	#each line of the input file is read and moved into a list and has
	#the newline character removed
	answerInput = []
	for item in examAnswers:
		item = item.strip()
		answerInput.append(item)

	#The list of correct answers is set up
	correctAnswerList = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']

	#The inputted answer list and correct answer list are returned to main
	return answerInput, correctAnswerList

#main controls the overall structure of the program
def main():

	#init is called, returning the list of user answers and the list of correct answers
	answerInput, correctAnswerList = init()

	#calcs is called with the user answer list and correct answer list as input. It then returns a counter of correct answers, incorrect answers and a list of the incorrect questions
	correctAnswers, incorrectAnswers, incorrectAnswerList = calcs(answerInput, correctAnswerList)

	#output is called with the correct and incorrect answer counters and incorrect question list and input
	output(correctAnswers, incorrectAnswers, incorrectAnswerList)

	#calcs handles all calculations for the program
def calcs(answerInput, correctAnswerList):
	#counters are set up for num of correct and incorrect answers
	correctAnswers = 0
	incorrectAnswers = 0

	#an empty list is set up to hold which questions are answered incorrectly
	incorrectAnswerList = []

	#the user answers are checked against the correct answers.
	for x in range(0, 20):
		if correctAnswerList[x] == answerInput[x]:
			#for each correct answer the correct answer counter is added to
			correctAnswers += 1
		else:
			#for each incorrect answer the question num is added to the end of a list and the incorrect answer counter is added to
			incorrectAnswerList.append(x + 1)
			incorrectAnswers += 1
	
	#the correct answer, incorrect answer and incorrect question list is returned to main
	return correctAnswers, incorrectAnswers, incorrectAnswerList

#output deals with printing data from the program
def output(correctAnswers, incorrectAnswers, incorrectAnswerList):

	#if the user had 15 or more correct answers the program displays a message that you passed as well as statistics of your answers
	if correctAnswers >= 15:
		print('*****************')
		print('~  YOU PASSED!  ~')
		print('*****************\n')

		#the program displays how many questions were answered correctly and incorrectly
		print('You answered', correctAnswers, 'question(s) right!')
		print('You answered', incorrectAnswers, 'question(s wrong!')

		#if the user had a perfect score...
		if correctAnswers == 20:
			#nothing else is printed. Otherwise...
			pass
		else:
			#a list of the questions answered incorrect are printed
			print('You answered these questions wrong: ', end = '')
			print(*incorrectAnswerList, sep = ', ')
	#if the user had 16 or more wrong answers the program displays a message that you passed as well as the statistics of your answers		
	else:
		print('*****************')
		print('~  YOU FAILED!  ~')
		print('*****************\n')

		#the program displays how many questions were answered correctly, incorrectly and a list of the questions answered incorrectly
		print('You answered', correctAnswers, 'question(s) right!')
		print('You answered', incorrectAnswers, 'question(s wrong!')
		print('You answered these questions wrong: ', end = '')
		print(*incorrectAnswerList, sep = ', ')

#main is called, which executes the whole program
main()