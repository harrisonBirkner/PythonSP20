#This program asks the user to enter the square feet of wall space to be painted and the price of the paint per gallon.
#The program should display the following data:
#    The hours of labor required
#    The cost of the paint
#    The labor charges 
#    The number of gallons of paint required
#    The total cost of the paint job

def inputValues():
#inputValues asks the user for the square feet of wall space needed painting and the price of paint per gallon and returns the results to main.
    iSqFt = float(input('Please input the square feet of wall that needs painting: '))
    iPricePerGal = int(input('Please input the price of the paint per gallon: '))
    return iSqFt, iPricePerGal

def calcs(iSqFt, iPricePerGal):
#calcs calculates the various amounts to be displayed by the program
    cGals = iSqFt / 112
    cTime = cGals * 8
    cPaintCost = iPricePerGal * cGals
    cLaborCost = cTime * 35
    cTotalCost = cLaborCost + cPaintCost
    return cTime, cGals, cPaintCost, cLaborCost, cTotalCost

def output(cTime, cGals, cPaintCost, cLaborCost, cTotalCost):
#output prints and formats all the appropriate data
    print('The job will require ' + format(cGals,',.2f') + ' gallons of paint.')
    print('The job will take ' + format(cTime,',.1f') + ' hours to complete.')
    print('The cost of paint will be $' + format(cPaintCost,',.2f'))
    print('The labor charge will be $' + format(cLaborCost,',.2f'))
    print('The total cost of the paint job will be $' + format(cTotalCost,',.2f'))

def main():
#main controls the overall structure/loop of the program
    iKeepGoing = '1'
    while iKeepGoing == '1':
        iSqFt, iPricePerGal = inputValues()

        cTime, cGals, cPaintCost, cLaborCost, cTotalCost = calcs(iSqFt, iPricePerGal)

        output(cTime, cGals, cPaintCost, cLaborCost, cTotalCost)

        iKeepGoing = input("Enter 0 to exit, 1 to continue ")

main()
