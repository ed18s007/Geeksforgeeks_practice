 # Count Pairs whose sum is equal to X 
def countPair(h1,h2,n1,n2,x):
    '''
    h1:  head of linkedList 1
    h2:  head of linkedList 2
    n1:  len of  linkedList 1
    n2:   len of linkedList 1
    X:   given sum
    '''
    if(n2==0 or n1==0):
        return 0
    node1, node2 = h1, h2
    cnt,set1 = 0, set()
    while node1:
        set1.add(node1.data)
        node1 = node1.next
    while node2:
        if((x - node2.data) in set1):
            cnt+=1
        node2 = node2.next
    return cnt