idList = []
passwordList = []

#this try/except clause checks for errors opening the dat file
try:
	loginInfo = open('password.dat', 'r')
except IOError:
	print("ERROR! There was an issue opening the file 'password.dat'.")

def mainMenu():
	print('\n\n*****MAIN MENU*****')
	print('*ENTER 1 TO SIGN IN\n')
	print('*ENTER 2 TO CREATE NEW USER\n')
	print('*ENTER 3 TO RESET PASSWORD\n')
	print('*ENTER 4 TO EXIT PROGRAM\n\n')
	while True:
		try:
			userOption = int(input('OPTION: '))
			if userOption == 1:
				signIn()
			elif userOption == 2:
				newUser()
			elif userOption == 3:
				resetPassword()
			elif userOption == 4:
				pass
			else:
				raise ValueError
			break
		except ValueError:
			print('ERROR! Input must be 1-3')


def signIn():
	print('\n\n*****SIGN IN*****')
	inputId = input('Enter login id: ')
	if inputId in idList:
		pass
	else:
		print('No matching login id found. Returning to menu...\n')
		mainMenu()

	inputPassword = input('\nEnter password: ')
	if inputPassword == passwordList[idList.index(inputId)]:
		pass
	else:
		print('Password does not match the login id entered. Returning to menu...\n')
		mainMenu()

	print('You have successfully been logged in!')
	
	input('Press enter to return to the main menu...')
	mainMenu()

def newUser():
	print('\n\n*****NEW USER*****')
	newId = input('Enter login id: ')
	valIdFlag = False
	valPassFlag = False
	while valIdFlag == False:
		newId, valIdFlag = validateId(newId, valIdFlag)
	print('Login id valid!')
	newPass = input('Enter password: ')
	while valPassFlag == False:
		newPass, valPassFlag = validatePass(newPass, valPassFlag, newId)
	print('Password valid!')
	appendNewLogin(newId, newPass)
	input('login id and password saved! Press enter to return to the main menu...\n')
	mainMenu()

def appendNewLogin(newId, newPass):
	idList.append(newId)
	passwordList.append(newPass)

	loginInfo.write(newId + '\n')
	loginInfo.write(newPass + '\n')

def validateId(newId, valIdFlag):
	if len(newId) > 5 and len(newId) < 11:
		pass
	else:
		newId = input('Login id is too short or long. 6-10 characters required. Try again: ')
		return newId, valIdFlag

	loginIdNumCtr = 0
	for x in newId:
		if x.isdigit():
			loginIdNumCtr += 1

	if loginIdNumCtr >= 2:
		pass
	else:
		newId = input('Login id does not have enough numbers. At least two numbers required. Try again: ')
		return newId, valIdFlag

	for x in newId:
		if x.isspace:
			pass
		else:
			newId = input('Login id has spaces. No spaces allowed. Try again: ')
			return newId, valIdFlag

	if newId not in idList:
		pass
	else:
		newId = input('Login id already exists. Try again: ')
		return newId, valIdFlag

	valIdFlag = True
	return newId, valIdFlag

def validatePass(newPass, valPassFlag, newId = None):
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

	if newPass not in newId:
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
	
def main():
	init()
	mainMenu()


main()