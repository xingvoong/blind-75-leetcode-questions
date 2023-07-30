'''
given 2 two integers a and b, return the sum of the 2 integers without
using the operators + and - 

example 1:
input: a = 1, b = 2
output: 3

example 2:
input: a = 2, b = 3
output: 5

-1000 <= a, b <= 1000
'''

def getSum(a,b):
    x, y = abs(a), abs(b)

    # ensure x >= y

    if x < y:
        return self.getSum(b, a)
    
    sign = 1 if a > 0 else - 1

    if a * b >= 0:
        # sum of two positive integers x + y
        # where x > y
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
    else:
        # difference of 2 integers x - y
        # where x > y

        while y:
            answer = x ^ y
            borrow = ((~x) & y) << 1
            x, y = answer, borrow
    
    return x * sign


def getSum(a, b):
    mask = 0xFFFFFFFF

    while b != 0:
        a, b = (a ^ b) & mask, ((a&b) << 1) & mask


    max_int = 0x7FFFFFFF

    return a if a < max_int else ~(a^mask)






