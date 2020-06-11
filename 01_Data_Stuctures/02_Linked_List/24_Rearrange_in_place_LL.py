 Rearrange linked list in-place 
def inPlace(root):
    #code here
    curr_node = root
    ls = []
    while curr_node:
        ls.append(curr_node.data)
        curr_node = curr_node.next
    n = len(ls)
    pt1, pt2 = 1,n-1
    while pt1<n-1:
        val = ls.pop()
        ls.insert(pt1,val)
        pt1+=2
    curr_node = root
    i = 0
    while curr_node:
        curr_node.data = ls[i]
        i+=1
        curr_node = curr_node.next
    return root