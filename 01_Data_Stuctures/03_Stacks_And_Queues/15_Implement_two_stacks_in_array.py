 Implement two stacks in an array 
 
def pop1(a):
    #code here
    i = 0
    while True:
        if a[i]==-1:
            break
        i+=1
    if i==0:
        return -1
    i-=1
    val = a[i]
    a[i] = -1
    return val
    
def pop2(a):
    #code here
    i = 100
    while True:
        if a[i]==-1:
            break
        i-=1
    if i==100:
        return -1
    i+=1
    val = a[i]
    a[i] = -1
    return val
    
def push1(a,x):
    #code here
    i = 0
    while True:
        if a[i]==-1:
            a[i]=x
            break
        i+=1
    
def push2(a,x):
    #code here
    i = 100
    while True:
        if a[i]==-1:
            a[i]=x
            break
        i-=1

