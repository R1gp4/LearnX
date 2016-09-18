#problem3test.py

s = 'boblkjbobjlksdbobobobjflksjdfowejajajssssss'

count = 0
word = 'abcdefghijklmnopqrstuvwxyz'
for i in range(len(s)):
	#print(s[i:i+3])
	if s[i:i+3] == word:

print("Longest substring in alphabetical order is: " , count)

'''

PROBLEM 3 

Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc


================= TRY ONE =================================

string = randomlettersinnonalphabeticalorder
word  = abcdefghijklmnopqrstuvwxyz

look in length of string, character by character, until end.
see if character corresponds with part of word. 
if yes, 
see if next character corresponds to word, this time only looking at the characters in string that come after.

answer is:  
print answer

'''