 # Node at a given index in linked list 
def getNth(head, k):
    # Code here
    if(k==1):
        return head.data
    else:
        node = head
        while k>1:
            node = node.next
            k-=1
        return node.data