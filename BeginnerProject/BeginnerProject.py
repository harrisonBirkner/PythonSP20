#This is a comment

print('Hello Sunshine!')
print("my first project.")
print('Mark said, "get it done".')
print('''Mark said, "let's get it done".''')
print('''one
		two
		three''')
print('one','two','three')
print('one','two','three',sep='')
print('one','two','three',end='')
print('one','two','three',sep='**@@**')
print('Monday\t\tTuesday\t\tWednesday')

# \t Tab
# \n Next line
# \' Print apostrophe
# \" Print double quote
# \\ Print backslash

print('Enter the amount of ' + 
		'sales for each day and press enter.')

print(format(123412345.6789, ',.2f'))
print('the number is', format(12345.6789, '12,.2f'))
print(format(0.5,'%'))
print(format(0.5,'.0%'))
print(format(0.5,'.2%'))

print(format(123456,'d'))
print(format(123456,',d'))
print(format(123456,'20,d'))
print(format(123456,'20,'))

name='Harrison'
print(name)

iAnswer = input("What is your name? ") #User entered data is always string
print(iAnswer)

hours = int(input("How many hours did you work? "))
payRate = float(input("What is your hourly pay rate? "))

pay = hours * payRate
print('$'+format(pay, ',.2f'))

iResult = float(hours) #Explicit override

x=5
if x == 4:
	print("yippee")
	x+=1
print(x)

# >, <, >=, <=, ==, !=

name = input("plase enter your name")
if name == "Willy":
	print("Willy saves the day")
else:
	print("Where is Willy?")

minSalary = 30000
minYears = 2	

salary = float(input("Enter your annual salary: "))
yearsOnJob = int(input("Enter your number of years employed: "))

if salary >= minSalary:
	if yearsOnJob >= minYears:
		print("You are loan worthy")
	else:
		print("You must have been employed for at least ", minSalary, "years to qualify")
else:
	print("You must earn at least $", format(minSalary,',.2f'),"per year to qualify")
	
grade = 'B'

if grade = 'A':
	print("Cool!")
elif grade = 'B':
	print("Good job!")
elif grade = 'C':
	print("Okay")
elif grade = 'D':
	print("Whew")
else:
	print("So sorry, so sad!")
		
keepGoing = True
while keepGoing:
	sales = float(input('Enter the amount of sales: '))
	commRate = float(input('Enter the commision rate: '))
	commision = sales * commRate
	print("the commision is $", format(commsion, '10,.2f'),sep="")
	ans = input('Do you want to calculate another commision? (Enter n for no): ')
	if ans.upper() == 'N':
		keepGoing = False
print("Thanks for playing!")

for num in [1, 2, 3, 4, 5]:
	print(num)

for name in ['Winken', 'Blinken', 'Nod':]
	print(name)
	
for num in range(5):
	print(num)
	
for num in range(1,5):
	print(num)
	
for num in range(1,5,2):
	print('\n'num)

for num in range(1,6,2):
	print('\n'num)
	
for num in range(5,0,-1):
	print('\n'num)
	
#Funky Math

num = num + 1
print(num)
num += 1
print(num)
num -= 1
print(num)
num *= 5
print(num)
num %= 5
print(num)

print('This program displays a list of numbers')
print('starting at 1 and their squares.')
end = int(input('How high should I go? '))
print('\nNumber\tSquare')
print('-----------------')

total = 0

for number in range(1, end + 1):
	square = number**2
	print(number, '\t', format(square, '5,d'))
	total += square

print('Total:', '\t', format(total, '5,d'))









