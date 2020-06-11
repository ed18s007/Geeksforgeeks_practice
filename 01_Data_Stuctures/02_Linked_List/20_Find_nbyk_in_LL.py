 # Find n/k th node in Linked list 
 import math
class LinkedList:
    def __init__(self):
        self.head =None
    
    def insert(self,val):
        if self.head is None:
            self.head = Node(val)
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = Node(val)
            
    def fractionalNodes(self,k):
        #add code here
        curr_node = self.head
        n = 1
        while curr_node.next:
            n +=1
            curr_node = curr_node.next
        if(k==1):
            return curr_node
        nk = int(math.ceil(n/k)) - 1
        k_node = self.head
        while(nk>0):
            k_node = k_node.next
            nk-=1
        return k_node
