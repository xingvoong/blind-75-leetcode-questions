'''
You are climbing a staircase. It takes n steps to reach the top

Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top

Example 1:
input: n = 2
Output: 2
Explanation: there are 2 ways to climb to the top
1: 1 step + 1 step
2: 2 steps

example 2:
input: n = 3
output: 3
Explanation: there are three ways to climb to the top
1: 1 step + 1 step + 1 step
2: 1 step + 2 steps
3: 2 steps + 1 step
'''

def climbStairs(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # create dp table
        dp = [0] * (n + 1)

        # init start cases
        dp[1] = 1
        dp[2] = 2

        # dp cases
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2]

    print(dp)
    return dp[-1]

print(climbStairs(0))
print(climbStairs(1))
print(climbStairs(2))
print(climbStairs(3))


