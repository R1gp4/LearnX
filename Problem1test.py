s = 'boboboboblalala'
word = 'bob'
index = s.find(word[:])

print(index)

#another try I did earlier: it returns all the letters in the string 

s = 'boblkjjlksdbobobobjflksjdfowejajajssssss'
sub = 'bob'
count = 0
for sub in s:
	count += 1

print(count)
#prints all characters.... not what I wanted.

count = 0
for sub in s[0:2]:
	count += 1
print(count)

