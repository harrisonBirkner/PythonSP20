# Playing with list examples
# Susan Wilson
# 4/14/20

names = ["Willy", "Bill", "Ethel"]
info = [ "Bertha", 82, 143.27]

print(info)

numbers = list(range(5))
print(numbers)

numbers = [0] * 5
print(numbers)

numbers = [ 1,'a',4] * 3
print(numbers)

number =  [ 99, 100, 101, 102]
for n in numbers:
    print(n)

print(number[0], number[3])

index = 0
while index < 4 :
    print(number[index])
    index += 1

print("\n\n")
index = -1
while index > -5 :
    print(number[index])
    index -= 1

print("\n\n")
size = len(number)
index = 0

while index < size:
    print(number[index])
    index += 1

print("\n\n")
list1 = [ 1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2
print(list1)
print(list2)
print(list3)

print("\n\n")
list1 += list2
print(list1)
print(list2)

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
midDays = days[2:4]
print("\n\n")
print(midDays)

midDays = days[:2]
print("\n\n")
print(midDays)

midDays = days[5:]
print("\n\n")
print(midDays)

midDays = days[:]
print("\n\n")
print(midDays)

midDays = days[0:4:2]
print("\n\n")
print(midDays)

midDays = days[-5:]
print("\n\n")
print(midDays)

prodNums = ['V475', 'F987', 'Q143', 'R688']
search = input('Enter a product number: ')
if search in prodNums:
    print(search, 'was found in the list.')
else:
    print(search, 'was not found in the list.')





























