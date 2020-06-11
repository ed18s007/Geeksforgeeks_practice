 
 # Remove duplicates from an unsorted linked list 
 def removeDuplicates(head):
    #code here
    set1 = set()
    if(head is None):
        return head
    if(head.next is None):
        return head
    prev_node = head
    next_node = head.next
    set1.add(prev_node.data)
    while next_node:
        if next_node.data in set1:
            if next_node.next is None:
                prev_node.next = None
                return head
            next_node = next_node.next
            prev_node.next = next_node
        else:
            prev_node = next_node
            if next_node.next is None:
                return head
            set1.add(next_node.data)
            next_node = next_node.next

 # For sorted
 def removeDuplicates(head):
    #code here
    set1 = set()
    if(head is None):
        return head
    if(head.next is None):
        return head
    prev_node = head
    next_node = head.next
    while next_node:
        if prev_node.data == next_node.data:
            if next_node.next is None:
                prev_node.next = None
                return head
            next_node = next_node.next
            prev_node.next = next_node
        else:
            prev_node = prev_node.next
            if next_node.next is None:
                return head
            next_node = next_node.next
