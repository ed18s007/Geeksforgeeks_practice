 # Pairwise swap elements of a linked list 
 def pairWiseSwap(head):
    # code here
    prev_node = head
    if head is None:
        return head
    curr_node = head.next
    if head.next is None:
        return head
    while curr_node:
        if curr_node.next is None:
            curr_node.data, prev_node.data = prev_node.data, curr_node.data
            return head
        if curr_node.next.next is None:
            curr_node.data, prev_node.data = prev_node.data, curr_node.data
            return head
        curr_node.data, prev_node.data = prev_node.data, curr_node.data
        curr_node = curr_node.next.next
        prev_node = prev_node.next.next