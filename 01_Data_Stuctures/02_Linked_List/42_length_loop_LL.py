 # Find length of Loop 
 def countNodesinLoop(head):
    #Your code here
    dic = {}
    i = 0
    curr_node = head
    while curr_node:
        if curr_node in dic:
            return i - dic[curr_node]-1
        dic[curr_node] = i
        i += 1
        if curr_node.next is None:
            return 0
        curr_node = curr_node.next
    

