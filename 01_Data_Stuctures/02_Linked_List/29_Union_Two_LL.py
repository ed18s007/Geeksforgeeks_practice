 # Union of Two Linked Lists 
 
def union(head1,head2):
    #code here
    set1 = set()
    while head1:
        set1.add(head1.data)
        head1= head1.next
    while head2:
        set1.add(head2.data)
        head2= head2.next
    ls = list(set1)
    ls.sort()
    ll = LinkedList()
    for i in ls:
        ll.append(i)
    return ll.head