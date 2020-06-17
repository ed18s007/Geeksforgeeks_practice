 # Deque Implementations 

 '''
Function to push element to front
    * dq : dqueue in which element is to be pushed
    * x : element to be pushed
'''
def push_front_pf(dq,x):
    #code here
    dq.appendleft(x)
    

''' Function to pop element from back
    * dq : dqueue From which element is to be popped
'''
def push_back_pb(dq,x):
    #code here
    dq.append(x)
    
    
'''
Function to return element from front
    * dq : dqueue from which element is to be returned
'''
def front_dq(dq):
    #code here
    return -1 if not dq else dq[0]

'''
 Function to pop element from back
    * dq : dqueue From which element is to be popped

'''
def pop_back_ppb(dq):
    #code here
    if dq:
        dq.pop()

