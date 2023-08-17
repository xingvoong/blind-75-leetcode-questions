'''
Given head, the head of a linked list, determine if the linked list has
a cycle in it

There is a cyle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

return true if there is a cycle in the linked list. Otherwise, return false


- if there is a cycle, fast will meet slow at some point

- fast == null
- or fast.next == null
- just start at the begining

'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
def hasCycle(head):
    # empty list has no cycle
    if head == None:
        return False

    slow = head
    fast = head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False

'''
runtime: O(N + K)
=> O(N)
space: O(N)
=> O(N)

'''