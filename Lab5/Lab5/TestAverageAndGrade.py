#This program that asks the user to enter five test scores. The program displays a letter grade for each score and the average test score.  
def main():
#main controls the overall structure of the program
    score1, score2, score3, score4, score5 = userInput()
    score1, score2, score3, score4, score5, cAverage = calcAverage(score1, score2, score3, score4, score5)
    grade1 = determineGrade(score1)
    grade2 = determineGrade(score2)
    grade3 = determineGrade(score3)
    grade4 = determineGrade(score4)
    grade5 = determineGrade(score5)
    output(cAverage, grade1, grade2, grade3, grade4, grade5,
           score1, score2, score3, score4, score5)

def userInput():
#userInput asks the user to input 5 test scores and then returns them to main
    score1 = float(input('Please input the score for test 1: '))
    score2 = float(input('Please input the score for test 2: '))
    score3 = float(input('Please input the score for test 3: '))
    score4 = float(input('Please input the score for test 4: '))
    score5 = float(input('Please input the score for test 5: '))
    return score1, score2, score3, score4, score5

def calcAverage(score1, score2, score3, score4, score5):
#calcAverage sums the 5 scores from userInput, calculates the mean score, and returns it to main
    cAverage = (score1 + score2 + score3 + score4 + score5) / 5
    return score1, score2, score3, score4, score5, cAverage

def determineGrade(score):
#determineGrade determines the letter grade of a score and returns it to main
    if score > 89:
        grade = 'A'
    elif score > 79:
        grade = 'B'
    elif score > 69:
        grade = 'C'
    elif score > 59:
        grade = 'D'
    else:
        grade = 'F'

    return grade
        
def output(cAverage, grade1, grade2, grade3, grade4, grade5, score1, score2, score3, score4, score5):
#output formats and prints the average score, 5 test scores, letter grades, and prints them
    print('\n----------------------------------')
    print('Average test score: ' + format(cAverage, '.2f') + '%')
    print('----------------------------------')
    print('Test 1:\t\t' + format(score1,'6,.2f') + '%', grade1)
    print('Test 2:\t\t' + format(score2,'6,.2f') + '%', grade2)
    print('Test 3:\t\t' + format(score3,'6,.2f') + '%', grade3)
    print('Test 4:\t\t' + format(score4,'6,.2f') + '%', grade4)
    print('Test 5:\t\t' + format(score5,'6,.2f') + '%', grade5)
    print('----------------------------------')

main()
