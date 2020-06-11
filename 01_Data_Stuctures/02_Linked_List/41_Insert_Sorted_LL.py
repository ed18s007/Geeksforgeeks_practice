 Insert in a Sorted List 
def sortedInsert(head1,key):
    #code here
    node = Node(key)
    if head1.data>= key:
        node.next = head1
        head1 = node
        return head1
    prev_node = head1
    if head1.next is None:
        head1.next = node
        return head1
    curr_node = head1.next
    while curr_node:
        if curr_node.data >= key:
            prev_node.next = node
            node.next = curr_node
            return head1
        curr_node = curr_node.next
        prev_node = prev_node.next
    if curr_node is None:
        prev_node.next = node
        return head1
