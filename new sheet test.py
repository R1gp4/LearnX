
l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

def flatten(l):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    reduce(lambda x,y: x+y,l)

flatten(l)