 # Nth node from end of linked list 
 def getNthfromEnd(head,n):
    #code here
    idx = 1
    curr_node = head
    while idx < n:
        if(curr_node.next is None):
            return -1
        idx+=1
        curr_node = curr_node.next
    prev_node = head
    while curr_node:
        if curr_node.next is None:
            return prev_node.data
        curr_node = curr_node.next
        prev_node = prev_node.next
