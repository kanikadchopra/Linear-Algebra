  ## length(vec) will consume a Vector, vec, and return the length which is based 
## on taking the square root of the sum of the squared x-component of vec and 
## squared y-component of vec 
## length: Vector -> Float
## Examples:
## length(zerov) => 0.0
## length(smallv1) => 1.4142

def length(vec):
    a = vec.x ** 2 
    b = vec.y ** 2 
    return math.sqrt(a+b)

## Test 1 - zero vector
check.within("len1",length(zerov), 0.0, 0.0001)
## Test 2 - small sized vector
check.within("len2", length(smallv1), 1.4142, 0.0001)
## Test 3 - medium sized vectors
check.within("len3", length(mediumv1), 18.0278, 0.0001)
## Test 4 - large vectors 
check.within("len4", length(largev1), 461.41088, 0.0001)
## Test 5 - v1 is negative 
check.within("len5", length(negv1), 5.8310, 0.0001)
## Test 6 - x-component of v1 is negative,y-component is positive 
check.within("len6", length(halfnegv1), 5.0990, 0.0001)
## Test 11 - y-component of v1 is negative, x-component is positive 
check.within("len7", length(neghalfv1), 5.3852, 0.0001)
