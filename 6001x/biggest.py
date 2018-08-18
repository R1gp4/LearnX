def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    r = []
    c = []
    for value in aDict.keys():
        if (c == []):
            c = value
            if (len(r) < len(c)):
                r = c
                c = value
            else:
                c = value
    if (len(c) > len(r)):
        r = c
    return(r)


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    result = None
    biggestValue = 0
    for key in aDict.keys():
        if len(aDict[key]) >= biggestValue:
            result = key
            biggestValue = len(aDict[key])
    return result