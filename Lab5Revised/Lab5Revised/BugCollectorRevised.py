#This program asks the user to input the number of bugs they 
#caught each day durig the week and calculates the total 
#number of bugs caught that week.

#Harrison Birkner 3/26/20

# main controls the overall structure and loop of the program
def main():
    bugTotal = 0

    for days in range(1,8):
        bugsToday = userInput()
        bugTotal += bugsToday
    output(bugTotal)

# userInput takes the users input and checks for exceptions
def userInput():

    # this try except returns an error if the user inputs non 
    # numeric data, sets the input variable to 0, and returns it
    # to the main
    try:
        bugsToday = int(input('How many bugs did you collect today? '))
    except ValueError:
        print("ERROR! Value must be numeric.")
        bugsToday = 0
    finally:
        return bugsToday

# output takes the accumulated bugs and formats and prints it.
def output(bugTotal):
    print('You collected', format(bugTotal,','), 'bugs this week!')

main()