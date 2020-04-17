#This program will ask the user for the number of males and the number of females registered in a class.
#The program should display the percentage of males and females in the class.

numMales = int(input("How many males are registered in the class? "))
numFemales = int(input("How many females are registered in the class? "))

totalStudents = numFemales + numMales

percMales = numMales / totalStudents
percFemales = numFemales / totalStudents

print('\nPercentage of males\tPercentage of females')
print(format(percMales,'19.1%')+'\t'+format(percFemales,'21.1%'))