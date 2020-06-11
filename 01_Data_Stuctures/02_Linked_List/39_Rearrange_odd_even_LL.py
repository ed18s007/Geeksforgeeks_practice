 # Rearrange a linked list odd even
def rearrangeEvenOdd(head):
    #code here
    odd = head
    if head.next is None:
        return odd
    even = head.next
    ret_even = head.next
    if even.next is None:
        return odd
    while True: 
        if even.next is None:
            odd.next = ret_even
            return head
        if even.next.next is None:
            odd.next = even.next
            even.next = None
            odd = odd.next
            odd.next = ret_even
            return head
        temp = even.next.next
        odd.next = even.next
        odd = odd.next
        even.next = temp
        even = even.next
        