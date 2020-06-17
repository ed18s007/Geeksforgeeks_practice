 # Implement stack using array 
 
class MyStack:
    
    def __init__(self):
        self.arr=[]
    
    #Adds element to the Stack
    def push(self,data):
        #add code here
        self.arr.append(data)
    
    #Removes element from the stack
    def pop(self):
        #add code here
        if len(self.arr) == 0 :
            return -1
        
        return self.arr.pop() 
