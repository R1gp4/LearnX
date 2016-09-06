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