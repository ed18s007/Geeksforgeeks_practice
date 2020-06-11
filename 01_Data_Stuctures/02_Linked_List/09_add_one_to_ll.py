def addOne(head):
    #Returns new head of linked List.
    current_node = head
    curr_str = ''
    while current_node:
        curr_str += str(current_node.data)
        current_node = current_node.next
    curr_int = int(curr_str) + 1
    new_str = str(curr_int)
    ll = LinkedList()
    for char in new_str:
        ll.insert(char)
    return ll.head

    