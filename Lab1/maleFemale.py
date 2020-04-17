numMales = int(input("How many males are registered in the class? "))
numFemales = int(input("How many females are registered in the class? "))

totalStudents = numFemales + numMales

percMales = numMales / totalStudents
percFemales = numFemales / totalStudents

print('\nPercentage of males\tPercentage of females')
print(format(percMales,'19.0%')+'\t'+format(percFemales,'21.0%'))