 # Reverse a linked list 
 def reverseList(self):
    # Code here
    if self.head is None:
        return None
    curr_node = self.head
    ls = []
    while curr_node:
        ls.append(curr_node.data)
        curr_node = curr_node.next
    curr_node = self.head
    while curr_node:
        curr_node.data = ls.pop()
        curr_node = curr_node.next