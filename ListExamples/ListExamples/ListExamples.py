evenNumbers = [12, 4, 6, 10]
print(evenNumbers)

names = ["Molly", "Pip", "Ethel" ]
print(names)

numbers = list(range(5))
print(numbers)

numbers = [0] * 5
print(numbers)

numbers = [1, 2, 3] * 3
print(numbers)

numbers = [99, 100, 101, 102]
for n in numbers:
    print(n)

print ('--------------------------')

myList = [10,20, 30, 40]
print(myList[0], myList[1], myList[2], myList[3])

index = 0
while index < 4:
    print(myList[index])
    index += 1

print(myList[-1], myList[-2], myList[-3], myList[-4])

size = len(myList)
index = 0
while index <len(myList):
    print(myList[index])
    index +=1

print ("*******************")
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8] 
list3 = list1 + list2

print(list1)
print(list2)
print(list3)

list2 += list1 
print(list2)

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
midDays=days[2:4]
print(midDays)

midDays=days[:2]
print(midDays)

midDays=days[5:]
print(midDays)

midDays=days[:]
print(midDays)

midDays=days[0:4:2]
print(midDays)

midDays=days[::2]
print(midDays)

print(days[-5:])

print("$$$$$$$$$$$$$$$$$$$$$$$")
prodNums = ['V475', 'F987', 'Q143', 'R688']
searchVar = input('Enter a product number: ')
if searchVar in prodNums:
    print(searchVar, 'was found in the list.')
else:
    print(searchVar, 'was NOT found in the list.')
    
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")

nameList =[ ]   #Creates an empty list
again = 'y'

while again == 'y':
    name = input("enter a name: ")
    nameList.append(name)     #Adds user entered name to the end of the list

    print('Do you wish to add another name? ')
    again = input('y = yes, anthing else = no: ')
    print()
print('Here are the names you entered.')
for name in nameList:
    print(name)
