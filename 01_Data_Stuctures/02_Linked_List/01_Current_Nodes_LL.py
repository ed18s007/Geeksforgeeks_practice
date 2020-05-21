def getCount(head_node):
    #code here
    current_node = head_node
    length = 0
    while current_node:
        length += 1
        current_node = current_node.next
    return length