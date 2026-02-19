#Grade Point Average calculator made by CYBIKAL corp.

import jdatetime

def moadelCalc(n):
    weight = 0
    gradeSum = 0
    weightSum = 0

    for i in range(n):
        print('\n')
        weight = int(input(f'Enter lesson {i+1} weight: '))

        while weight < 1 or weight > 3:
            print('!!! Invalid weight !!!')
            weight = int(input(f'Enter lesson {i+1} weight: '))
        weightSum = weightSum + weight

        grade = int(input(f'Enter lesson {i+1} grade: '))

        while grade > 20 or grade < 0:
            print('!!! Invalid grade !!!')
            grade = int(input(f'Enter lesson {i+1} grade: '))
        gradeSum = gradeSum + (weight * grade)
        
    termAverage = gradeSum / weightSum
    return termAverage
    
print('**********************************')
print('***Welcome to Moadel Calculator***')
print('**********************************')

print('Today is: ' + str(jdatetime.datetime.now()))

num = int(input('\nPlease enter the number of your lessons(-1 to exit): '))

while(num != -1):
    if num >= 1 and  num <= 10:
        average = moadelCalc(num)
        print('\nYour Grades Point Average will be: ', average)
        break
    else:
        print('!!! Invalid number of lessons !!!')
        num = int(input('\nPlease enter the number of your lessons(-1 to exit): '))

print('\nThank you for using GPA calculator!\nSee ya later..\nCYBIKAL corp.\n')