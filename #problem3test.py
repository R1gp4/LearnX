#problem3test.py
# Paste your code into this box
s= 'saderjlsjeroseijasdfkjsdfisnfseils'


print('a' < 'b')

'''

s = 'abcboblkjbobjlksdbobobobjflksjdfowejajajsabcsssss'

print("Longest substring in alphabetical order is: ")
count = 0
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for i in range(len(s)):
	ans = ''
	if s[i:i] == alphabet[i:i]:
		ans = ans + s[i]
		print(ans)

	else:
		print("naahh")


		





PROBLEM 3 

Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc


================= TRY ONE =================================

string = randomlettersinnonalphabeticalorder
alphabet  = abcdefghijklmnopqrstuvwxyz

look in length of string, character by character, until end.
see if character corresponds with character in alphabet. 
if yes, print letter, and  look in the rest of the string
see if next character corresponds to alphabet, 
if not move to the next character in the string.




an_letters = "aefhilmnorsxAEFHILMNORSX”
word = input("I will cheer for you! Enter a word: ")
times = int(input("Enthusiasm level (1-10): "))
i = 0
whilei < len(word):
	char = word[i]
	if char in an_letters:
		print("Give me an " + char + "! " + char)
	else:
		print("Give me a " + char + "! " + char)
		i += 1
print("What does that spell?”)
	for i in range(times):
		print(word, "!!!”)


		'''