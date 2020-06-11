 # Delete node in Doubly Linked List 
 # Your task is to complete this function
# function should just delete the Node
# function shouldn't print or return any data
def deleteNode(head, x):
    # Code here
    if(x==1):
        curr_node = head.next
        curr_node.prev = None
        head = curr_node
    else:
        i=1
        curr_node = head
        while i<x-1:
            curr_node = curr_node.next
            i +=1
        next_node = curr_node.next
        if(next_node.next is None):
            curr_node.next = None
        else:
            curr_node.next = next_node.next