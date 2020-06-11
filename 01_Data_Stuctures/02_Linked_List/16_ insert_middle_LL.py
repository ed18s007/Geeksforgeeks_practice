 # Insert in Middle of Linked List 
 # 	Function Arguments: head (head of linked list), node (node to be inserted in middle)
	# Return Type: None, just insert the new node at mid.
 def insertInMid(head,node):
    #code here
    slow_node, fast_node = head, head
    if(slow_node.next is None):
        slow_node.next = node
    else:
        while fast_node.next is not None:
            if(fast_node.next.next is None):
                break
            fast_node = fast_node.next.next
            slow_node = slow_node.next
        next_node = slow_node.next
        slow_node.next = node
        node.next = next_node