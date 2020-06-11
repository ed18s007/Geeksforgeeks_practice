# Detect Loop

def detectLoop(head):
    #code here
    slow = head
    fast = head
    if slow.next is None:
        return False
    if fast.next.next is None:
        return False
    if slow.next == slow:
        return True
    while True:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
        if fast.next is None:
            return False
        if fast.next.next is None:
            return False