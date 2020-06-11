 Delete Middle of Linked List 
 def deleteMid(head):
    '''
    head:  head of given linkedList
    return: head of resultant llist
    '''
    
    #code here
    slow_node = head
    if(slow_node is None):
        return head
    fast_node = head
    if(fast_node.next is None or fast_node.next.next is None):
        head.next = None
        return head
    while fast_node.next:
        slow_node = slow_node.next
        if(fast_node.next.next is None):
            break
        fast_node = fast_node.next.next
    slow_node.data = slow_node.next.data
    slow_node.next = slow_node.next.next
    return head