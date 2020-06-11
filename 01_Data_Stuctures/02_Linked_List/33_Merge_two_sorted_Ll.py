 Merge two sorted linked lists
def merge(head_a,head_b):
    #code here
    temp = None
    
    if head_a is None:
        return head_b
    
    if head_b is None:
        return head_a
    
    if head_a.data <= head_b.data:
        temp = head_a
        
        temp.next = merge(head_a.next,head_b)
    
    else:
        temp = head_b
        
        temp.next = merge(head_a,head_b.next)
    
    return temp



 def merge(head_a,head_b):
    #code here
    merged = LinkedList()

    while (head_a and head_b):
        if(head_a.data < head_b.data):
            merged.append(head_a.data)
            head_a = head_a.next
            if(head_a is None):
                while head_b:
                    merged.append(head_b.data)
                    head_b = head_b.next
        else:
            merged.append(head_b.data)
            head_b = head_b.next
            if(head_b is None):
                while head_a:
                    merged.append(head_a.data)
                    head_a = head_a.next
    return merged.head