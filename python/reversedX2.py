# Test projects of season 1 python course

x = int(input('Please enter your wished number: '))

yekan = x % 10
dahgan = (x // 10) % 10
sadgan = x // 100

newNum = str(yekan) + str(dahgan) + str(sadgan)
newNum = int(newNum)

print('Your reversed number is: ' + str(newNum))
print('Your reversed x 2 result will be: ' + str(newNum * 2))
