# -*- coding: utf-8 -*-
"""
Created on Wed Jan 14 18:51:07 2026

Doing 650 Q's'
Word counter

@author: Kiarash
"""

userString = 'Be Iran salam o be Tehran salam bad!'

counts = dict()
words = userString.split()
basket = list()

for word in words:
    if word in basket:
        counts[word] += 1
    else:
        counts[word] = 1
    basket.append(word)

#print(counts.items())
#keys = list(counts.keys())
#values = list(counts.values())
print('Words   |    Reps\n------------------')
for key, val in counts.items() :
    print(key,' ---> ', val)
