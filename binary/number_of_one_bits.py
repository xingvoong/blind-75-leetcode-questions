'''
write a function that takes an unsigned integer and returns the number
of '1' bits it has (also known as the Hamming weight)

constraints:
- the input must be a binary string of length 32


'''

def hammingWeight(n):
    ans = 0
    while n > 0:
        if n % 2 == 1:
            ans += 1
        n = n//2
    return ans


print(hammingWeight(3))
print(hammingWeight(100))
print(hammingWeight(4294967293))

def hammingWeight2(n):
    count = 0
    while n != 0:
        n &= n - 1
        count += 1
    return count

print(hammingWeight2(3))
print(hammingWeight2(100))
print(hammingWeight2(4294967293))

'''
the run time depends on the number of 1-bits in n.
In the worse case, all bits in n are 1-bits.
In case of a 32-bit integer, the run time is O(1)
1111111111111111 => O(1) still

'''