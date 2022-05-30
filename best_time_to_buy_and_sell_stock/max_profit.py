'''
you are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock

Return the maxinum profit you can achieve from this transaction.  if you cannot achieve any profit, return 0

'''

'''
- get the min price first, and keep update this
- get the max price after the current min price
- return the max_profit = current_price - min_price


'''
def max_profit(prices):
    min_price = prices[0]
    max_profit = 0
    for i in range(len(prices)):
        max_profit = max(prices[i] - min_price, max_profit)
        min_price = min(min_price, prices[i])
    return max_profit


print(max_profit([7, 1, 5, 3, 6, 4]))
print(max_profit([7,6,4,3,1]))

'''
run time: O(N)
space: O(1)
'''