s = 'boblkjbobjlksdbobobobjflksjdfowejajajssssss'
count = 0
word = 'bob'
for i in range(len(s)):
	print(s[i:i+3])
	if s[i:i+3] == word:
		count += 1

print(count)



#Tries
'''
s = 'boboboboblalala'
word = 'bob'
index = s.find(word[:])

print(index)

#something I tried earlier: this returns 0.

s = 'boblkjjlksdbobobobjflksjdfowejajajssssss'
sub = 'bob'
count = 0
for sub in s:
	count += 1

print(count)

#another try I did earlier: it returns all the letters in the string 

count = 0
for sub in s[0:2]:
	count += 1
print(count)

#prints out 2, which is just as weird as it counting all the characters.

count = 0

for word in s:
	if word == 'b':
		if  word == 'o':
			if word == 'b':
				count += 1
print(count)

# this gives back zero, probably because word can't be all three characters at once

count = 0

for n in range(3):
	if n == 'bob':
		count += 1

print(count)

#I feel like I'm closer here but I'm not gettin the result yet. time for a break time: 21:52

counter = 0
for i in range(0,+1):
	if s == 'bob':
		counter += 1

print(counter)

#somehow I want to get my scope/searchlight to 3 and my increment to 1.0

print(len(s))


word = 'bob'
print(s[:3])

count = 0
while(s[0:3] == word):
		count += 1
		break
		
print(count) 


s = 'boblkjbobjlksdbobobobjflksjdfowejajajssssss'
count = 0
a = 0
x = 3
print(s[a:x])

word = 'bob'
for n in range(len(word)):
	if s[a:x] == word:
		count += 1
		x += 1
		a += 1
	else: 
		x += 1
		a += 1
	
print(a)
print(x)
print(s[a:x])

print(count)


s = 'boblkjbobjlksdbobobobjflksjdfowejajajssssss'
count = 0
word = 'bob'
for i in range(len(s)):
	print(s[i:i+3])
	if s[i:i+3] == word:
		count += 1

print(count)



'''

	