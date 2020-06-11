 # Given a linked list of 0s, 1s and 2s, sort it. 
''
def segregate(head):
    #code here
    zero, one, two = 0,0,0
    curr_node = head
    while curr_node:
        if(curr_node.data == 0):
            zero+=1
        elif(curr_node.data == 1):
            one +=1
        else:
            two +=1
        curr_node = curr_node.next
    curr_node = head
    while curr_node:
        while(zero>0):
            zero-=1
            curr_node.data = 0
            curr_node = curr_node.next
        while(one>0):
            one-=1
            curr_node.data = 1
            curr_node = curr_node.next
        while(two>0):
            two-=1
            curr_node.data = 2
            curr_node = curr_node.next
    return head



 def segregate(head):
    #code here
    zero, one, two = None, None, None
    curr_node = head
    while curr_node:
        if(curr_node.data==0):
            if zero is None:
                zero = curr_node
                zero_head = zero
            else:
                zero.next = curr_node
                zero = zero.next
        elif(curr_node.data==1):
            if one is None:
                one = curr_node
                one_head = one
            else:
                one.next = curr_node
                one = one.next
        elif(curr_node.data==2):
            if two is None:
                two = curr_node
                two_head = two
            else:
                two.next = curr_node
                two = two.next
        curr_node = curr_node.next
    zero.next = one_head
    one.next = two_head
    return zero_head
