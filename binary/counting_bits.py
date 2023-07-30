'''
given an integer n, return an array of length n + 1 such that for each i (0 <= i <= n),
ans[i] is the number of 1's in the binary representation of i

Example 1:

input: n = 2
Output: [0, 1, 1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

example 2:
Input: n = 5
Output: [0, 1, 1, 2, 1, 2]
Explanation:

0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

step 1: write pop count
step 2: write loop to count each integer

'''

def countBits(n):

    def pop_count(x):
        count = 0
        while x != 0:
            x &= x - 1 # zeroing out the least significant non zero bit
            count += 1
        return count

    ans = [0] * (n + 1)
    for x in range(n + 1):
        ans[x] = pop_count(x)

    return ans


print(countBits(2))
print(countBits(5))

'''
time: O(NlogN)

for each integer x, in the worst case, we need to perform O(logn)
operations, since the number of bits in x equals to logx + 1 and all the bits
can be equal to 1. However, on average, each bit will be set n/2 times,
so for each integer x we will perform log(x)/2 operations, therefor in total,
it will cost O(n.log(n)/2) operations
- space: O(1), since the out
'''