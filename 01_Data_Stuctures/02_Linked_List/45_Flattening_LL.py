 # Flattening a Linked List 
 
def flatten(root):
    #Your code here
    curr_node = root
    ls = []
    while curr_node:
        bot_node = curr_node
        while bot_node:
            ls.append(bot_node.data)
            bot_node = bot_node.bottom
        curr_node = curr_node.next
    ls.sort()
    head = None
    for i in ls:
        if head is None:
            head = Node(i)
            curr = head
        else:
            head.bottom = Node(i)
            head = head.bottom
    return curr

