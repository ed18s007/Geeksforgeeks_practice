 # Modular Node 
 def modularNode(head, k):
    #function should return the modular Node
    #if no such node is present then return -1
    curr_node = head
    n = 1
    if(curr_node is None):
        return -1
    while curr_node.next:
        n +=1
        curr_node = curr_node.next
    if(k>n):
        return -1
    if(k==n):
        return curr_node.data
    idx = (n//k)*k
    curr_node = head
    while(idx>1):
        idx-=1
        curr_node = curr_node.next
    return curr_node.data