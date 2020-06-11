 Reverse a Doubly Linked List 
def reverseDLL(head):
    #return head after reversing
    curr_node = head
    ls = []
    while curr_node:
        ls.append(curr_node.data)
        curr_node = curr_node.next
    curr_node=head
    while curr_node:
        curr_node.data = ls.pop(-1)
        curr_node = curr_node.next
    return head

def reverseDLL(head):
    #return head after reversing
    curr_node = head
    if curr_node is None or curr_node.next is None:
        return head
    prev_node = head
    curr_node = head.next
    prev_node.next = None
    prev_node.prev = curr_node
    while curr_node.next:
        next_node = curr_node.next
        curr_node.prev = next_node
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node
    curr_node.next = prev_node
    curr_node.prev =None
    return curr_node