'''
a while loop to go to n
- make a node to link the n+1 node after
- disconnect n node with n + 1
- disconnect n - 1 with n
- connect n - 1 with n + 1

if the length of the list is k
nth node from the end of the list
is the (k - n) node from the begining of the list

'''

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def removeNthFromEnd(head, n):

    count = length = 1
    ptr = l = head

    while l.next:
        length += 1
        l = l.next
    
    if length == 1 and n == 1:
        return None
    
    if length == n:
        return head.next

    while count < length - n:
        ptr = ptr.next
        count += 1
    
    ptr.next = ptr.next.next

    return head
    

