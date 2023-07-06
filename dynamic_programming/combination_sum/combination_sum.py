'''
Example 1:
Input: candidates = [2, 3, 6, 7], target = 7
Output: [[2, 2, 3], [7]]

Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7/
These are the only 2 combinations.

Example 2:
input: candidates = [2, 3, 5], target = 8
output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

Example 3:
input: candidates = [2], target = 1
output: []

'''

def combinationSum(candidates, target):
    n =  len(candidates)
    result = []

    def backtracking(remain_sum, combo, start_index):
        if remain_sum == 0:
            result.append(list(combo))
        elif remain_sum < 0:
            return
        else:
            for i in range(start_index, n):
                # place the next candidate:
                combo.append(candidates[i])

                # backtracking, explore after placing that candidate
                backtracking(remain_sum - candidates[i], combo, i)

                # revert previous choice for other exploration
                combo.pop()

    # starting call for backtracking
    backtracking(target, [], 0)
    return result


print(combinationSum([2, 3, 6, 7], 7))
print(combinationSum([2, 3, 5], 8))
