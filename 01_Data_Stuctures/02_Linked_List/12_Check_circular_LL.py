# your task is to complete this function
# function should return true/false or 1/0
def isCircular(head):
    # Code here
    slw_node, fst_node = head,head
    while fst_node.next is not None:
        slw_node = slw_node.next
        if(fst_node.next.next is None):
            return False
        fst_node = fst_node.next.next
        if(slw_node==fst_node):
            return True

