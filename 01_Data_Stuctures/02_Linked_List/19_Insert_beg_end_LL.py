 # Linked List Insertion 
# function should insert new node at the
# beigning of the list
def insertAtBegining(a,value):
    #code here
    if(a.head is None):
        a.head = Node(value)
        a.tail = a.head
    else:
        new_node = Node(value)
        new_node.next = a.head
        a.head = new_node
    
# function should insert new node at the
# end of the list
def insertAtEnd(a,value):
    #code here too :)
    curr_node = a.head
    if(curr_node is None):
        a.head = Node(value)
        a.tail = a.head
    else:
        a.tail.next = Node(value)
        a.tail = a.tail.next