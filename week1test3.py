# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 07:54:32 2016

@author: Roman
"""

s = 'cyqfjhabcdefgcclkbxpbojgkar'
r = ''
c = ''
for char in s:
    if (c == ''):
        c = char
    elif (c[-1] <= char):
        c += char
    elif (c[-1] > char):
        if (len(r) < len(c)):
            r = c
            c = char
        else:
            c = char
if (len(c) > len(r)):
    r = c
print(r)