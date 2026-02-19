# python training(Income Calculator)

import re

def incomeCalculator(incomePerHour, workingDays):
    workingHours = 0
    for day in range(workingDays):
        startAndFinish = input(f'Enter start and finish hours for day {day+1} (start-finish): ')
        flag = re.search(r'(\d{1,2}\.\d{1,2}).+?(\d{1,2}\.\d{1,2})',startAndFinish)
        if flag:
            startHour, finishHour = flag.groups()
            startHour = float(startHour)
            finishHour = float(finishHour)
            print(f'start hour : {startHour}')
            print(f'finish hour : {finishHour}')
            print(f'hours worked in the day : {finishHour - startHour}')
        else:
            print('Invalid format entered!!!')
        workedHours = finishHour - startHour
        workingHours += workedHours
    income = workedHours * incomePerHour
    print(f'\nYour income for this month is ${income} dollars!')

print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
print('$$$$$& Welcome to Income Calculator $$$$$$$')
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n')

monthDays = int(input('How many days were in this month? '))
daysOff = int(input('How many days you took off? '))
incomePerHour = int(input('How much is your income per hour? '))

print('\nCalculating your income...\n')
incomeCalculator(incomePerHour,monthDays - daysOff)
