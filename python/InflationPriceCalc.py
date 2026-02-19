# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 02:37:12 2026

Inflation

@author: Kiarash
"""
currentYear = 1404
price = int(input('Enter price(toman): '))
years = int(input('Enter years: '))
inflationRate = int(input('Enter inflation rate(%): '))
    
print('Year    |    Price')
print('-------------------')

for year in range(1, years):  
    currentYear +=1
    price = price + (price * (inflationRate/100))

    print(f'{currentYear}       {price}')