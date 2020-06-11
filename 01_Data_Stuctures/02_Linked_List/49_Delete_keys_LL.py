 # Delete keys in a Linked list 
 
def deleteAllOccurances(head, k):
    # Code here
    prev_node = head
    if(prev_node.data == k):
        while prev_node.data == k:
            if prev_node.next is None:
                return None
            prev_node = prev_node.next
        head = prev_node
    curr_node = head.next
    if curr_node is None:
        return head
    while curr_node:
        if curr_node.data == k:
            while curr_node.data == k:
                if curr_node.next is None:
                    prev_node.next = None
                    return head
                curr_node = curr_node.next
            prev_node.next = curr_node
        prev_node = prev_node.next
        curr_node = curr_node.next
    return head