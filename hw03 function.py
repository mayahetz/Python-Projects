#hw03 function 

def computePower(base, power):
    ''' 
    takes in a base integer and its power (positive integer including 0), and 
    returns the number to its power (base ^ power)
    '''

    if power == 0:  #base case because anything ^0 = 1
        return 1 
    else:
        return base * computePower(base, power-1)


assert computePower(3,0) == 1
assert computePower(3,3) == 27
assert computePower(-2,3) == -8
assert computePower(0,3) == 0