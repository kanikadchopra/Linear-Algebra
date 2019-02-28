## This file will be the code for adding vectors and multiplying by scalar multiplication.

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
          
    
## Constant Vectors:
zerov = Vector(0,0)
smallv1 = Vector(1,1)
smallv2 = Vector(2,2)
mediumv1 = Vector(10, 15)
mediumv2 = Vector(25, 20)
largev1 = Vector(400, 230)
largev2 = Vector(133, 240)
negv1 = Vector(-5, -3)
negv2 = Vector(-2, -6)
halfnegv1 = Vector(-1, 5)
halfnegv2 = Vector(-2, 7)
neghalfv1 = Vector(5, -2)
neghalfv2 = Vector(7, -3)

## This code is for adding two vectors together:

## add_vectors(v1, v2) consumes two Vectors, v1, and v2 and returns a new Vector
## that is the vector addition of v1 and v2. Vector addition is adding the 
## x-component of v1 to the x-component of v2 and similarly for the y-component 
## of v1 and v2
## add_vectors: Vector Vector -> Vector
## Examples:
## add_vectors(Vector(0,0), Vector(0,0)) => Vector(0,0)
## add_vectors(Vector(1,2), Vector(4,2)) => Vector(5,4)    

def add_vectors(v1,v2):
    
    first = v1.x + v2.x
    second = v1.y + v2.y
    new = Vector(first, second)
    
    return new

## Test 1 - zero vectors for both
check.expect("addt1", add_vectors(zerov, zerov), zerov)
## Test 2 - v1 is zero vector 
check.expect("addt2", add_vectors(zerov, smallv1), smallv1)
## Test 3 - v2 is zero vector 
check.expect("addt3", add_vectors(smallv2, zerov), smallv2)
## Test 4 - both are not the zero vector (small number) - scalar multiples
check.expect('addt4', add_vectors(smallv1, smallv2), Vector(3,3))
## Test 5 - medium sized vectors
check.expect('addt5', add_vectors(mediumv1, mediumv2), Vector(35,35))
## Test 6 - large vectors 
check.expect('addt6', add_vectors(largev1,largev2), Vector(533, 470))
## Test 7 - v1 is negative 
check.expect("addt7", add_vectors(negv1,smallv1), Vector(-4,-2))
## Test 8 - v2 is negative 
check.expect("addt8", add_vectors(smallv2, negv2), Vector(0,-4))
## Test 9 - both are negative vectors 
check.expect("addt9", add_vectors(negv1, negv2), Vector(-7, -9))
## Test 10 - x-component of v1 is negative,y-compoennt is positive 
check.expect("addt10", add_vectors(halfnegv1, smallv2), Vector(1,7))
## Test 11 - x-component of v2 is negative, y-component is positive 
check.expect("addt11", add_vectors(mediumv1, halfnegv2), Vector(8, 22))
## Test 12 - x-component of v1 is positive, y-component is negative
check.expect("addt12", add_vectors(neghalfv1, mediumv2), Vector(30,18))
## Test 13 - x-component of v2 is positive, y-component is negative 
check.expect("addt13", add_vectors(smallv1, neghalfv2), Vector(8, -2))

## This code below is for scalar multiplication:

## scale(vec,k) consumes a Vector, vec, and an Integer, k, and mutates vec by 
## multiplying the x-component and the y-component of vec by k 
## Effects:
## ** vec is mutated by a scalar value of k 
## scale: Vector Int -> None 
## Examples:
## scale(zerov, 2) => None 
## zerov => zerov
## scale(smallv1, 2) => None
## smallv1 => Vector(2,2)

def scale(vec,k):
    first = k * vec.x
    second = k * vec.y
    vec.x = first
    vec.y = second 
    
vec1 = Vector(0,0)
## Test 1 - zero vector
check.expect("scale1", scale(vec1, 2), None)
check.expect("vec1", vec1, zerov)

vec2 = Vector(1,1)
## Test 2 - k is zero 
check.expect("scale2", scale(vec2, 0), None)
check.expect("vec2", vec2, zerov)

vec3 = Vector(1,1) 
## Test 3 - k is 1, Vector is (1,1)
check.expect("scale3", scale(vec3, 1), None)
check.expect("vec3", vec3, vec3)

vec4 = Vector(1,1)
## Test 4 - vec is Vector(1,1) and k is >1
check.expect("scale4", scale(vec4, 4), None)
check.expect("vec4", vec4, Vector(4,4))

vec5 = Vector(2,4)
## Test 5 - small sized vector, small k 
check.expect("scale5", scale(vec5, 2), None)
check.expect("vec5", vec5, Vector(4,8))

vec6 = Vector(10,25)
## Test 6 - medium vector, medium k
check.expect("scale6", scale(vec6, 10), None)
check.expect("vec6", vec6, Vector(100,250))

vec7 = Vector(100, 250)
## Test 7 - large vector, large k
check.expect("scale7", scale(vec7, 200), None)
check.expect("vec7", vec7, Vector(20000, 50000))

vec8 = Vector(-1, -2) 
## Test 8 - vec is negative, k is positive
check.expect("scale8", scale(vec8, 2), None)
check.expect("vec8", vec8, Vector(-2,-4))

vec9 = Vector(2,4)
## Test 9 - k is negative, vec is positive
check.expect("scale9", scale(vec9, -2), None)
check.expect("vec9", vec9, Vector(-4,-8))

vec10 = Vector(-2, -4)
## Test 10 - vec and k are both negative
check.expect("scale10", scale(vec10, -2), None)
check.expect("vec10", vec10, Vector(4, 8))

vec11 = Vector(-1,5)
## Test 11 - x-component of v1 is negative,y-component is positive, k negative
check.expect("scale11", scale(vec11,-2), None)
check.expect("vec11", vec11, Vector(2, -10))

vec12 = Vector(5,-2)
## Test 12 - y-component of v1 is negative, x-component is positive, k negative
check.expect("scale12", scale(vec12,-3), None)
check.expect("vec12", vec12, Vector(-15, 6))

vec13 = Vector(-1,5)
## Test 11 - x-component of v1 is negative,y-component is positive, k positive
check.expect("scale13", scale(vec13,2), None)
check.expect("vec13", vec13, Vector(-2, 10))

vec14 = Vector(5,-2)
## Test 12 - y-component of v1 is negative, x-component is positive, k positive
check.expect("scale14", scale(vec14,3), None)
check.expect("vec14", vec14, Vector(15, -6))