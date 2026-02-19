# Project recognizing aval number 

num = int(input('Please enter your number: '))
flag = False

while num != -1:
    if num == 1:
        print('Number 1 is NOT a prime number!\n')
    elif num > 1:
        for i in range(2, num):
            if (num % i == 0):
                flag = True
                break
            else:
                flag = False
        if flag:
            print('The number ' + str(num) + ' is NOT prime number!\n')
            #flag = False
        else:
            print('The number ' + str(num) + ' IS prime number!\n') 
    else:
        print('You have entered a negative number!\n')

    num = int(input('Enter a number again(-1 to exit): '))

print('Thank you for using CYBIKAL prime number detecter!\n See ya later..')

