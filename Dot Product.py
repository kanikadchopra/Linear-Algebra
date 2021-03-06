## This code is for calculating the dot product given two vectors. The following class is used for the vector calculations.

import check
import math

class Vector:
    '''Fields: x(Int), y(Int)'''
    def __init__(self,xVal,yVal):
        self.x = xVal
        self.y = yVal
        
    def __eq__(self,other):
        if isinstance(other,Vector):
            return self.x == other.x and self.y == other.y
        else:
            return False
        
    def __repr__(self):
        return "Vector({0},{1})".format(self.x,self.y)
          
## dot_product(v1,v2) consumes two vectors, v1 and v2, and returns an Integer 
## that is the made up of adding the product of the x-component of both vectors
## and the y-component of both vectors
## dot_product: Vector Vector -> Int 
## Examples:
## dot_product(zerov, zerov) => 0
## dot_product(Vector(1,2), Vector(4,2)) => 8

def dot_product(v1,v2):
    return (v1.x*v2.x) + (v1.y * v2.y)

## Test 1 - zero vectors for both
check.expect("dot1", dot_product(zerov, zerov), 0)
## Test 2 - v1 is zero vector 
check.expect("dot2", dot_product(zerov, smallv1), 0)
## Test 3 - v2 is zero vector 
check.expect("dot3", dot_product(smallv2, zerov), 0)
## Test 4 - both are not the zero vector (small number) - scalar multiples
check.expect('dot4', dot_product(smallv1, smallv2), 4)
## Test 5 - medium sized vectors
check.expect('dot5', dot_product(mediumv1, mediumv2), 550)
## Test 6 - large vectors 
check.expect('dot6', dot_product(largev1,largev2), 108400)
## Test 7 - v1 is negative 
check.expect("dot7", dot_product(negv1,smallv1), -8)
## Test 8 - v2 is negative 
check.expect("dot8", dot_product(smallv2, negv2), -16)
## Test 9 - both are negative vectors 
check.expect("dot9", dot_product(negv1, negv2), 28)
## Test 10 - x-component of v1 is negative,y-component is positive 
check.expect("dot10", dot_product(halfnegv1, smallv2), 8)
## Test 11 - x-component of v2 is negative, y-component is positive 
check.expect("dot11", dot_product(mediumv1, halfnegv2), 85)
## Test 12 - x-component of v1 is positive, y-component is negative
check.expect("dot12", dot_product(neghalfv1, mediumv2), 85)
## Test 13 - x-component of v2 is positive, y-component is negative 
check.expect("dot13", dot_product(smallv1, neghalfv2), 4)