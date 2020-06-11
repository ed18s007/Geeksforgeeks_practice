 # Delete nodes having greater value on right 
 def compute(head):
    #Your code here
    prev_node = head
    if head.next is None:
        return head
    curr_node = head.next
    while curr_node:
        if curr_node.next is None:
            if prev_node.data < curr_node.data:
                prev_node.next = None
                return head
        if prev_node.data < curr_node.data:
            curr_node = curr_node.next
            prev_node.next = curr_node
        else:
            prev_node = prev_node.next 
            curr_node = curr_node.next
