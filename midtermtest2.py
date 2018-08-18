
l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

def flatten(l):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
	reduce(lambda x, y: x.extend(y), l)

    

flatten(l)












stuff = "iQ"

for thing in stuff:
        if thing == 'iQ':
           print("Found it")

           

def Square(x):
	
	return(SquareHelper(abs(x), abs(x)))


def SquareHelper(n, x):
    if n == 0:
        return 0
    return(SquareHelper(n-1, x) + x)

Square(-5)




listA = [1, 2, 3, ['a', 'b', 'c']]
listB = [4, 5, 6]

listC = listA[::-1]

print(listC)


	inter_dict = {}
	diff_dict = {}

	for key, value in d1.items():
	    if key in d2.keys():
	        # keys are shared
	        inter_dict[key] = f(value, d2[key])
	    else:
	        # d1 contains a key not found in d2.
	        # add this to diff_dict
	        diff_dict[key] = value

	for key, value in d2.items():
	    if key not in d1.keys():
	        # d2 contains a key not found in d1.
	        # add this to diff_dict
	        diff_dict[key] = value

	return (interdict, diff_dict)

