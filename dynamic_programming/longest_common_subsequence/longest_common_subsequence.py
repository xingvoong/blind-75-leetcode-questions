from functools import lru_cache

def longestCommonSubsequene(text1, text2):

    @lru_cache(maxsize=None)
    def memo_solve(p1, p2):

        #base case: if either string is now empty,
        # we can't make up anymore characters.

        if p1 == len(text1) or p2 == len(text2):
            return 0
        
        # option 1: we don't include text(1) o1 in the solution 
        option_1 = memo_solve(p1 + 1, p2)

        # option 2: we include text1[p1] in the solution, as long as a match ofr it in text 2 or after p2 exists
        firsy_coccurence = text2.find(text1[p1], p2)
        option_2 = 0
        if first_occurence != -1:
            option_2 = 1 + memo_solve(p1+1, first occurence + 1)
        
        # return the best option
        return max(option_1, option_2)
    
    return memo_solve(0, 0)