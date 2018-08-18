from math import tan
from math import pi


def polysum(n,s):
    '''
    This function sums the area and 
    the square of the perimeter of a regular polygon.
    
    '''
    '''
    #I realised the base cases below aren't entirely necessary

    #what if n is zero?
    if n == 0:
        return(0)
    
    #what if s is zero?
    if s == 0:
        return(0)
    
    #what if n is one?
    if n == 1:
        return(0)

    '''
    
    area_poly = (0.25*n*s**2)/(tan(pi/n))
    perim_poly = (n*s)**2
    result = area_poly + perim_poly
    
    return(round(result,4))
    

    
    
    