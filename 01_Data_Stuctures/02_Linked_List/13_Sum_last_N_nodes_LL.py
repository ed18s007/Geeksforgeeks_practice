 # Find the Sum of Last N nodes of the Linked List 
def sumOfLastN_Nodes(head,n):
    #function should return sum of last n nodes
    curr_node, prev_node = head, head
    i= n
    tot = 0
    while i>0:
        tot += curr_node.data
        curr_node = curr_node.next
        i-=1
    if(curr_node is None):
        return tot
    else:
        while curr_node is not None:
            curr_node = curr_node.next
            prev_node = prev_node.next
        tot = 0
        while prev_node is not None:
            tot += prev_node.data
            prev_node = prev_node.next
        return tot
        