# #python training..

class Car:
    count = 0
    def __init__(self,name,speed,price):
        self.name = name
        self.speed = speed
        self.price = price

    def priceIncrease(self,increasement):
        self.price += increasement

    def carInfo(self):
        print(f'Car name --> {self.name}')
        print(f'Car speed --> {self.speed} mph')
        print(f'Car price --> ${self.price}')

    def priceUpdate(self):
        print(f'{self.name} car price is : ${self.price}')

BMW = Car('BMW',180,250000)
Lambo = Car('Lamborghini',200,400000)
Bugatti = Car('Bugatti',250,1000000)
Benz = Car('Mercedes-Benz',175,200000)

carsList = [BMW,Lambo,Bugatti,Benz]

print('*************Welcome**************')
print('****************To****************')
print('*************CYBIKAL**************')
print('**********Auto-Gallery************\n')

choice = input('Enter the name of the car you are looking for to increase the price: ')

while choice != '-1':
    flag = False
    for cars in carsList:
        if choice == cars.name:
            flag = True
            picked = cars
            break
    if flag:
        print(f'Car info : ')
        picked.carInfo()
        increasement = int(input('How much do you want to increase the price of the car? '))
        picked.priceIncrease(increasement)
        print(f'New price for {picked.name} car is ${picked.price}')

        choice = input('\nEnter the Car name to increase the price(-1 to exit): ')
    else:
        print('The car was not found')
        choice = input('Which car to increase the price(-1 to exit): ')

print('\nNew cars price list: ')
BMW.priceUpdate()
Lambo.priceUpdate()
Benz.priceUpdate()
Bugatti.priceUpdate()

print('\nThank you for using CYBIKAL Auto Gallery software..\n')


# class Car:
#     count = 0
#     def __init__(self, name, speed, price):
#         self.name = name
#         self.speed = speed
#         self.price = price

#     def priceIncrease(self, increasement):
#         self.price += increasement

#     def carInfo(self):
#         print(f'Car name --> {self.name}')
#         print(f'Car speed --> {self.speed} mph')
#         print(f'Car price --> ${self.price}')

# BMW = Car('BMW', 180, 250000)
# Lambo = Car('Lamborghini', 200, 400000)
# Bugatti = Car('Bugatti', 250, 1000000)
# Benz = Car('Mercedes-Benz', 175, 200000)

# carsList = [BMW, Lambo, Bugatti, Benz]

# print('*************Welcome**************')
# print('****************To****************')
# print('*************CYBIKAL**************')
# print('**********Auto-Gallery************\n')

# choice = input('Enter the name of the car you are looking for to increase the price: ')

# while choice != '-1':
#     found = False
#     for car in carsList:
#         if choice == car.name:
#             picked = car
#             found = True
#             break
#     if found:
#         print(f'Car info : ')
#         picked.carInfo()
#         increasement = int(input('How much do you want to increase the price of the car? '))
#         picked.priceIncrease(increasement)
#         print(f'New price of {picked.name} is ${picked.price}')
#     else:
#         print('Car not found!')
#     choice = input('What car are you looking for (-1 to exit): ')







































# class pySolution:
#     count = 0
#     def __init__(self,numList,target):
#         self.numList = numList
#         self.target = target
    
#     def problemSolver(self):
#         for i in listOfNumbers:
#             for j in listOfNumbers:
#                 if i + j == inputTarget:
#                     print(f'Result numbers are : {i} & {j}')
#                     listOfNumbers.clear()
#                     # listOfNumbers.remove(i)
#                     # listOfNumbers.remove(j)
#                 # else: 
#                 #     print(f'No numbers were found to sum up to {inputTarget} !!!')

# print('*********WELCOME*********')

# number = int(input('Please enter a number(only 2-digits): '))
# listOfNumbers = []
# while number != -1:
#     if number > 9 and number < 100:
#         listOfNumbers.append(number)
#         number = int(input('Enter a number again(-1 to exit): '))
#     else:
#         print('Wrong input!!!')
#         number = int(input('Enter a number again(-1 to exit): '))

# inputTarget = int(input('Enter your wished target number: '))

# print('Your list of numbers:',listOfNumbers)
# print('Your target is:',inputTarget)

# if listOfNumbers:
#     p1 = pySolution(listOfNumbers,inputTarget)
#     p1.problemSolver()

# print('\nThank you for using Target Software...\n')