 # Finding middle element in a linked list 
# function should return index to the any valid peak element
def findMid(head):
    # Code here
    slw_node, fst_node = head,head
    while (fst_node.next is not None):
        slw_node = slw_node.next
        if(fst_node.next.next is None):
            return slw_node
        fst_node = fst_node.next.next
    return slw_node

