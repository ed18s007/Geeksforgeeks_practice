
 # Merge 2 sorted linked list in reverse order 
 def mergeResult(h1,h2):
    #return head of merged list
    node1, node2 = h1,h2
    ls = []
    while node1:
        ls.append(node1.data)
        node1=node1.next
    while node2:
        ls.append(node2.data)
        node2=node2.next
    ls.sort(reverse=True)
    ll = Llist()
    tail = None
    for i in ls:
        tail = ll.insert(i,tail)
    return ll.head
