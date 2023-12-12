'''
- find the middle node of the linked list
in 1->2->3->4->5->6 find 4

slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

- reverse the second haft:
prev, cur = None, slow
while cur:
    cur, prev,cur = prev, cur, cur.next

- merge 2 sorted list into 1 list (not sorted)
first, second = head, prev
while second.next:
    first.next, first = second, first.next
    second.next, second = first, second.next

'''

def reorderlist(head):

    if not head:
        return

    # find the middle node
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # reverse the second haft
    prev, cur = None, slow
    while cur:
        cur.next, prev, cur = prev, cur, cur.next

    # merge 2 sorted list, into 1 not sorted list
    first, second = head, prev
    while second.next:
        first.next, first = second, first.next
        second.next, second = first, second.next


'''
runtime: O(N)
space: O(1)
'''
