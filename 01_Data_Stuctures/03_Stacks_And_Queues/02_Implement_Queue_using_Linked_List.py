 Implement Queue using Linked List 
# A linked list (LL) node 
# to store a queue entry 
class Node: 
      
    def __init__(self, data): 
        self.data = data 
        self.next = None
        
class MyQueue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    
    # Method to add an item to the queue
    def push(self, item): 
         
         #Add code here
        if self.head is None:
            self.head = Node(item)
            self.tail = self.head
        else:
            self.tail.next = Node(item)
            self.tail = self.tail.next
        
    
    # Method to remove an item from queue
    def pop(self):
         
        #add code here
        if self.head is None:
            return -1
        else:
            val = self.head.data
            if self.head==self.tail:
                self.head = None
            else:
                self.head = self.head.next
            return val
