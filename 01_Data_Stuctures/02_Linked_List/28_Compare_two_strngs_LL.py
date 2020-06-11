 # Compare two linked lists 
 def compare(head1, head2):
    #return 1/-1/0
    while True:
        if(ord(head1.data)>ord(head2.data)):
            return 1
        elif(ord(head1.data)<ord(head2.data)):
            return -1
        elif(ord(head1.data)==ord(head2.data)):
            head1 = head1.next
            head2 = head2.next
            if((head1 is None) and (head2 is None)):
                return 0
            elif (head1 is None):
                return -1
            elif (head2 is None):
                return 1