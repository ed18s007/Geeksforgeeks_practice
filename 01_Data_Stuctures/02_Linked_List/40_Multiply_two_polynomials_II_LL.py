# Multiply two polynomials II 

def proOfPolynomials(head1,head2,n1,n2):
    #return head of resultant linked list
    ls = [0]*(n1+n2-1)
    ls1 = []
    ls2 = []
    while head1:
        ls1.append(head1.data)
        head1 = head1.next
    while head2:
        ls2.append(head2.data)
        head2 = head2.next
    j = 0
    for i in range(n1):
        elem = ls1[i]
        for k in range(j,j+n2):
            ls[k] += elem*ls2[k-j]
        j+=1
    ll = Llist()
    tail = None
    for a in ls:
        tail = ll.insert(a,tail)
    return ll.head
    

