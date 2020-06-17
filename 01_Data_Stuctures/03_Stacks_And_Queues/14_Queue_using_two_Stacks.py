 # Queue using two Stacks 
def qPush(x,stack1,stack2):
    '''
    x: value to push
    stack1: list
    stack2: list
    '''
    
    #code here
    stack1.append(x)

def qPop(stack1,stack2):
    
    '''
    stack1: list
    stack2: list
    '''
    
    #code here
    if len(stack1)==0:
        return -1
    for i in range(len(stack1)):
        stack2.append(stack1.pop())
    val = stack2.pop()
    for i in range(len(stack2)):
        stack1.append(stack2.pop())
    return val

