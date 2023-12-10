'''
- use 2 pointers
- maintain the distance of 2 pointers by n
- move first pointer to n + 1
- keep second pointer at 1
- if the count is greater then n + 1
- then move first pointer to n
- and go second.next = second.next.next
- 2 pointers technique

'''

def removeNthFromEnd(head, n):

    first = second = head
    count = 1

    while first.next:
        count += 1
        first = first.next

        if count > n + 1:
            second = second.next

    if count == n:
        return head.next
    else:
        second.next = second.next.next

    return head