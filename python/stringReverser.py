# -*- coding: utf-8 -*-
"""
Created on Wed Jan 14 19:26:59 2026

@author: Kiarash
"""

str1 = input('Enter a phrase : ')
reversedStr = str()
length = len(str1)
for char in range(len(str1)-1, -1, -1):
    reversedStr += str1[char]


#while length > 0:
#    reversedStr += str1[length-1]
#    length -= 1

print('Original phrase:',str1)
print('Reversed phrase:',reversedStr)