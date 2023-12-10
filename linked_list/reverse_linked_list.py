'''
Given the head of a singly linked list, reverse the list, and return the reversed list

input: head = [1, 2, 3, 4, 5]
ouput: [5, 4, 3, 2, 1]

input: head = [1, 2]
output: [2, 1]

example 3:
input: head = []
output: []

Algo:
1: empty list:
return

2: declare 3 new pointers to keep track 3 part of the linked list
- prev, current, next
- move them accordingly

3:
'''




def reverseList(head):
    if not head:
        return head

    prev = None
    current = head
    next = head.next

    while next:
        current.next = prev
        prev = current
        current = next
        next = next.next
    current.next = prev

    return current



