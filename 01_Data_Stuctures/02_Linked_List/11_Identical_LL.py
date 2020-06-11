 # Identical Linked Lists 

def areIdentical(head1, head2):
    # Code here
    while True:
        if(head1.data==head2.data):
            head1 = head1.next
            head2 = head2.next
        else:
            return False
        if((head1 is None) and (head2 is None)):
            return True
        