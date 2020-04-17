#This program asks the user to enter a month (in numeric form), a day, and a two-digit year.
#The program then determines whether the month times the day equals the year.
#If so, it displays a message saying the date is magic.
#Otherwise, it displays a message saying the date is not magic.

day = int(input('Please input a day: '))
month = int(input('Please input a month: '))
year = int(input('Please input a year: '))

testYear = day * month

if testYear == year:
    print('Your date is magic!')
else:
    print("Your date isn't magic")
