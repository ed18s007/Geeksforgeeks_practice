 # Polynomial Addition 
 
# return a linked list denoting the sum with decreasing value of power
def addPolynomial(poly1, poly2):
    # Code here
    ls = []
    while poly1:
        l = [poly1.coef, poly1.power]
        ls.append(l)
        poly1 = poly1.next
    while poly2:
        l = [poly2.coef, poly2.power]
        ls.append(l)
        poly2 = poly2.next
        
    ls = sorted(ls, key= lambda x: x[1], reverse=True)
    ll = Linked_List()
    i = 0
    while i<len(ls)-1:
        if ls[i][1] == ls[i+1][1]:
            co = ls[i][0]+ls[i+1][0]
            ll.insert(co,ls[i][1])
            i +=2
        else:
            ll.insert(ls[i][0],ls[i][1])
            i+=1
    if i<len(ls):
        ll.insert(ls[i][0],ls[i][1])
    return ll.head