'''
You are given the heads of two sorted linked lists list1 and list2

Merge the 2 lists into one sorted list. The list should be made by splicing together
the nodes of the first two lists

Return the head of the merged linked list

I: 2 sorted linked lists
O: 1 sorted linked list
C: splicing them together
E:

example 1:
input: list1 = [1, 2, 4]
list2 = [1, 3, 4]
output: [1, 1, 2, 3, 4, 4


example 2:
input: list1 = [], list2 = []
output: []

example 3:
input: list1 = [], list2 = [0]
output: [0]

Constraints:
- the number of nodes in both lists is in the range [0, 50]
- -100 <= Node.val <= 100
- both list1 and lists2 are sorted in non-decreasing order
'''

'''
definition for singly-linked list
class ListNode:
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = next


Algo:
- need a head pointer stay unchange to return
- keep a current pointer to move in between lists        
'''

class Solution:
    def mergeTwoLists(l1, l2):
        # maintain an unchaning reference to node ahead
        # of the return node
        head = ListNode(-1)
        current = head
        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        
        if l1 is None:
            current.next = l2
        else:
            current.next = l1

        return head.next