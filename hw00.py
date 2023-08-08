x = 10 * 5 - 3 // 2
print(x)

y = 2 ** 4 / (4 + 4)
print(y)

def f(n):
    while n < 10:
        if n < 3:
            n = n + 2
        elif n < 6:
            return n
        if n < 10:
            n = n + 5
            return n
    return n

print(f(2))
print(f(5))
print(f(7))
print(f(9))
print(f(11))

def countOdds(a_list):
    ''' 
    takes a list of positive integers as its parameter and returns 
    the total number of odd values in the parameter list
    '''
    count = 0

    for number in a_list:
        if number % 2 != 0:
            count += 1
    return count

assert countOdds([1,2,3]) == 2
assert countOdds([]) == 0
assert countOdds([3,3,5]) == 3
