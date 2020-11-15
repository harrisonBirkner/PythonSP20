# This program demonstrates how the append
# method can be used to add items to a list
#
#Susan Wilson
#4/14/20

def main():
    #Create an empty list
    nameList = ['Sarah', 'Tom']

    #create a variable to control my loop
    playAgain  ='y'

    #Add names to my list
    while playAgain == 'y':
        name = input('Enter a name: ')

        #append the name to the list
        nameList.append(name)

        print('Do you want to add another name? ')
        playAgain = input('y = yes, anything else = no: ')
        print()

    #Display the names that were entered.
    print('Here are the names you entered')
    for name in nameList:
        print(name)

main()