'''
Given a string s containing just the characters '(', ')', '{', '}', '[', ']', determine if the input string is valid

An input string is valid if:
1: open brackets must be closed by the same type of brackets
2: open brackets must be closed in the correct order
3: every close bracket has corresponding open bracket of the same type

use a stack:
- when seeing a closing bracket, I need to pop it
'''


def isValid(s):

    stack = []

    if len(s) ==  1:
        return False

    # if s[0] == ']' or s[0] == '}' or s[0] == ')':
    #     return False

    for c in s:
        if c == '(' or c == '[' or c == '{':
            stack.append(c)

        # pop when seeing a closing bracket
        # if no more to pop it mean too many closing bracket
        # return false
        else:
            if len(stack) != 0:
                top = stack.pop()
            else:
                return False

            if c == ')' and top != '(':
                return False
            elif c == ']' and top != '[':
                return False
            elif c == '}' and top != '{':
                return False

    # in the end, the stack is empty
    if len(stack) != 0:
        return False
    return True

example = (([]))
s1 = "()"
s2 = "()[]{}"
s3 = "(()]"
s4 = "("
s5 = "(("
s6 = "){"
s7 = "()))"

print(isValid(s1))
print(isValid(s2))
print(isValid(s3))
print(isValid(s4))
print(isValid(s5))
print(isValid(s6))
print(isValid(s7))

'''
think more about test cases: edge case
time: O(N)
space: O(N)

'''