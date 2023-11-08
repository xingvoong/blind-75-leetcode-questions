'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order

An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Solution:
mainting a map of key - value
key is the first word I see of that order
value is that word, but in different arrangement of letters.

example
{
'bat': [bat],
'eat': [ate, eat, tea],
'nat': [nat, tan]
}

to do this, I need a dict of list, and I also need to sort the word
'''

def groupAnagram(strs):
    import collections

    # need to remember the syntax for creating
    # a non traditonal list
    d = collections.defaultdict(list)

    for word in strs:
        # need to convert sorted(word) to tuple because
        # a list is not hashable
        d[tuple(sorted(word))].append(word)

    return d.values()

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagram(strs))

'''
Let N is the length of strs
K is the maxinum length of a word

sorting take: O(KlogK)
for loop take: O(N)
runtime: O(NKlogK)

space: O(NK)
the length of strs and the length of each word, or maxinum word.

'''
