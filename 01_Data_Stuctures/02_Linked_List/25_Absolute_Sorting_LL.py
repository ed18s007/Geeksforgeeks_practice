 # Absolute List Sorting 
 def sortList(head):
    '''
    head: head of linkedList
    
    Your method shouldn't print anything
    it should transform the passed linked list
    '''
    curr_node = head
    ls = []
    while curr_node:
        ls.append(curr_node.data)
        curr_node = curr_node.next
    ls.sort()
    curr_node=head
    while curr_node:
        curr_node.data = ls.pop(0)
        curr_node = curr_node.next
