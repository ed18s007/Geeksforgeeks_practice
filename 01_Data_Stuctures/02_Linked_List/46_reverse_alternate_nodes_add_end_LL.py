 # Given a linked list, reverse alternate nodes and append at the end 
 def rearrange(head):
    # Code here
    prev_node = head
    curr_node = head.next
    if curr_node is None:
        return head
    if curr_node.next is None:
        return head
    temp = None
    while True:  
        if curr_node.next is None:
            curr_node.next = temp
            return head
        if curr_node.next.next is None:
            prev_node.next = curr_node.next
            prev_node = prev_node.next
            prev_node.next = curr_node
            curr_node.next = temp
            return head
        next_node = curr_node.next.next
        prev_node.next = curr_node.next
        prev_node = prev_node.next
        curr_node.next = temp
        temp = curr_node
        curr_node = next_node

