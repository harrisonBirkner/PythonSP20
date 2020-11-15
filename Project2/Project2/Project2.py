#This program displays a menu with 4 options: SIGN IN, CREATE NEW USER, RESET PASSWORD, AND EXIT PROGRAM. SIGN IN prompts the user to enter a login id and password that is checked against login data in the file.
#CREATE NEW USER prompts the user to enter a new login id and password that is added to the file. RESET PASSWORD prompts the user to enter their old password and new password which is added to the file. EXIT PROGRAM
# terminates the program.

#Harrison Birkner
#4/21/2020


#empty lists are created for ids and passwords. They are created globally because of frequency of use
idList = []
passwordList = []

#this try/except clause checks for errors opening the dat file
try:
	loginInfo = open('password.dat', 'r')
except IOError:
	#if an error is raised attempting to open the file a message is printed and the program is terminated 
	print("ERROR! There was an issue opening the file 'password.dat'.")
	exit(0)

#mainMenu displays the users options for that menu
def mainMenu():
	print('\n\n*****MAIN MENU*****')
	print('*ENTER 1 TO SIGN IN\n')
	print('*ENTER 2 TO CREATE NEW USER\n')
	print('*ENTER 3 TO RESET PASSWORD\n')
	print('*ENTER 4 TO EXIT PROGRAM\n\n')
	#this loop will run until a valid option is entered
	while True:
		try:
			userOption = int(input('OPTION: '))
			if userOption == 1:
				#on a 1 the sign in option is selected
				signIn()
			elif userOption == 2:
				#on a 2 the new user option is selected
				newUser()
			elif userOption == 3:
				#on a 3 the reset password option is selected
				resetPassword()
			elif userOption == 4:
				#on a 4 the exit program option is selected
				print('Program terminated')
				exit(0)
			else:
				#if an invaled option is entered an error is raised
				raise ValueError
			break
		except ValueError:
			print('ERROR! Input must be 1-3')

#signIn prompts the user to sign in by entering an existing login id and password
def signIn():
	print('\n\n*****SIGN IN*****')
	inputId = input('Enter login id: ')

	#if the inputted id exists in the file...
	if inputId in idList:
		#validation continues, otherwise...
		pass
	else:
		#an error is printed and the user is returned to the main menu
		print('No matching login id found. Returning to menu...')
		mainMenu()

	inputPassword = input('\nEnter password: ')
	#if the inputted password exists in the file...
	if inputPassword == passwordList[idList.index(inputId)]:
		#validation is finished, otherwise...
		pass
	else:
		#an error is printed and the user is returned to the main menu
		print('Password does not match the login id entered. Returning to menu...')
		mainMenu()

	print('You have successfully been logged in!')
	
	input('Press enter to return to the main menu...')
	mainMenu()

#newUser allows the user to enter a new login id and password
def newUser():
	print('\n\n*****NEW USER*****')
	newId = input('Enter login id: ')
	valIdFlag = False
	valPassFlag = False
	#while the new id is not valid the loop will continue
	while valIdFlag == False:
		#validateId is ran with the user's inputted id and the flag for if it is valid passed into it. It returns data into the two same variables
		newId, valIdFlag = validateId(newId, valIdFlag)
	print('Login id valid!')
	newPass = input('Enter password: ')
	#while the new password is not valid the loop will continue
	while valPassFlag == False:
		#validatePass is ran with the user's inputted password and the flag for if it is valid passed into it. It returns data into the two same variables
		newPass, valPassFlag = validatePass(newPass, valPassFlag, newId)
	print('Password valid!')

	#once validated the id and password are added to the list
	idList.append(newId)
	passwordList.append(newPass)

	appendNewLogin()

	input('login id and password saved! Press enter to return to the main menu...')
	mainMenu()

#resetPassword allows the user to reset an existing password
def resetPassword():
	print('\n\n*****RESET PASSWORD*****')
	oldPass = input('Please enter your old password: ')
	#this loop continues until the password entered is found in the list of existing passwords
	while True:
		if oldPass in passwordList:
			print('password found!')
			#the position of the old password in the list is found and moved into a variable
			passIndex = passwordList.index(oldPass)
			break
		else:
			oldPass = input('No matching password found. Try again: ')
		
	newPass = input('Please enter new password: ')

	valPassFlag = False
	#while the new password is not valid the loop will continue
	while valPassFlag == False:
		#validatePass is ran with the user's inputted password, the flag for if it is valid, and the login id matching the password passed into it. It returns data into the new password and password flag variable
		newPass, valPassFlag = validatePass(newPass, valPassFlag, idList[passIndex])
	
	#once validated the old password is changed to the new password
	passwordList[passIndex] = newPass
	appendNewLogin()

	input('Password successfuly changed! Press enter to return to the main menu...')
	mainMenu()

#this function overwrites password.dat with the current id and password lists
def appendNewLogin():
	#this try/except clause checks for errors opening the dat file
	try:
		loginInfo = open('password.dat', 'w')
	except IOError:
		#if an error is raised attempting to open the file a message is printed and the program is terminated
		print("ERROR! There was an issue opening the file 'password.dat'.")
		exit(0)
	
	#this loop runs for as many times as there are items in the id list (which list is chosen is arbitrary as they have the same number of items)
	for x in range(0, len(idList)):
		#the id with an index of x is written to the file concatenated with a newline character
		loginInfo.write(idList[x] + '\n')
		#the password with an index of x is written to the file concatenated with a newline character
		loginInfo.write(passwordList[x] + '\n')

	#password.dat is closed
	loginInfo.close

#validateId has an id and flag for id validity as arguments. If any validation returns false the id and flag are returned and the function exits
def validateId(newId, valIdFlag):
	#if id's length is 6-10...
	if len(newId) > 5 and len(newId) < 11:
		#nothing happens, otherwise...
		pass
	else:
		#an error message is displayed and the funcion exits
		newId = input('Login id is too short or long. 6-10 characters required. Try again: ')
		return newId, valIdFlag

	#counter for # of numbers in id is set to 0
	loginIdNumCtr = 0
	#this loops through the characters in the id
	for x in newId:
		#if the character is a digit...
		if x.isdigit():
			#one is added to the counter
			loginIdNumCtr += 1
	
	#if the id has at least two numbers...
	if loginIdNumCtr >= 2:
		#nothing happens, otherwise...
		pass
	else:
		#an error message is displayed and the funcion exits
		newId = input('Login id does not have enough numbers. At least two numbers required. Try again: ')
		return newId, valIdFlag

	#this loops through the characters in the id
	for x in newId:
		#if the character is not a space...
		if x.isspace:
			#nothing happens, otherwise...
			pass
		else:
			#an error message is displayed and the funcion exits
			newId = input('Login id has spaces. No spaces allowed. Try again: ')
			return newId, valIdFlag

	#if the id is not in the id list...
	if newId not in idList:
		#nothing happens, otherwise...
		pass
	else:
		#an error message is displayed and the funcion exits
		newId = input('Login id already exists. Try again: ')
		return newId, valIdFlag
	
	#once validation is complete the id validation flag is set to true and the flag and id are returned
	valIdFlag = True
	return newId, valIdFlag

#validatePass runs a password through validation and exits the function if any return false
def validatePass(newPass, valPassFlag, id = None):
	if len(newPass) > 5 and len(newPass) < 13:
		pass
	else:
		newPass = input('Password is too short or long. 6-12 characters required. Try again: ')
		return newPass, valPassFlag

	PassNumCtr = 0
	for x in newPass:

		if x.isdigit():
			PassNumCtr += 1

	if PassNumCtr >= 1:
		pass
	else:
		newPass = input('Password does not have enough numbers. At least one number required. Try again: ')
		return newPass, valPassFlag

	PassUpCtr = 0
	for x in newPass:
		if x.isupper():
			PassUpCtr += 1

	if PassUpCtr >= 1:
		pass
	else:
		newPass = input('Password does not have enough uppercase letters. At least one uppercase letter required. Try again: ')
		return newPass, valPassFlag

	PassLowCtr = 0
	for x in newPass:
		if x.islower():
			PassLowCtr += 1

	if PassLowCtr >= 1:
		pass
	else:
		newPass = input('Password does not have enough lowercase letters. At least one lowercase letter required. Try again: ')
		return newPass, valPassFlag

	for x in newPass:
		if x.isspace:
			pass
		else:
			newPass = input('Password has spaces. No spaces allowed. Try again: ')
			return newPass, valPassFlag

	if newPass not in id:
		pass
	else:
		newPass = input('Password cannot contain login id. Try again: ')
		return newPass, valPassFlag

	if newPass not in passwordList:
		pass
	else:
		newPass = input('Password already exists. Try again: ')
		return newPass, valPassFlag

	valPassFlag = True
	return newPass, valPassFlag

#createIdList reads a line from the file, strips it of newline character, and adds it to the id list
def CreateIdList():
	id = loginInfo.readline()
	id = id.rstrip('\n')
	if id == '':
		pass
	else:
		idList.append(id)
	return id

#init handles one time operations done at the beginning of the program
def init():
	id = CreateIdList()

	while id != '':
		password = loginInfo.readline()
		password = password.rstrip('\n')
		passwordList.append(password)
		
		id = CreateIdList()

	loginInfo.close

#main controls the overall structure of the program	
def main():
	init()
	mainMenu()


main()