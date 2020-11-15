daysWorked = int(input('How many days did you work? '))
totalPennies = 1

print(' Salary/Day ')
print('------------')
print('1 . $       0.01')

for day in range(2, daysWorked + 1):
    if totalPennies == 1:
        totalPennies = 2
        dailyPennies = 2
    else:
        dailyPennies *= 2
        totalPennies += dailyPennies

    print(day, '. $', format((dailyPennies / 100),'10,.2f'))

print('\nTotal Salary')
print('------------')
print('$', format(((totalPennies + 1) / 100), '10,.2f'))
