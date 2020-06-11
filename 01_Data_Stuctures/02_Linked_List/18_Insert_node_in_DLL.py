 # Doubly linked list Insertion at given position 
def addNode(head, p, data):
    # Code here
    idx = 0
    curr_node = head
    while idx<p:
        idx+=1
        curr_node = curr_node.next
    if(curr_node.next is None):
        curr_node.next = Node(data)
        curr_node.next.prev = curr_node
    else:
        next_node = curr_node.next
        curr_node.next = Node(data)
        curr_node.next.prev = curr_node
        curr_node.next.next = next_node
        next_node.prev = curr_node.next