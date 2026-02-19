# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 01:27:38 2026

@author: Kiarash
"""
# Mini bubble sort

a = int(input('Enter a value: '))
b = int(input('Enter b value: '))
c = int(input('Enter c value: '))

if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b
    
print('Sorted order is as follow :', a, b, c)