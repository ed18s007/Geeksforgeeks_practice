 # Pairwise Consecutive Elements 
# Function to check if elements are 
# pairwise consecutive in stack 
def pairWiseConsecutive(l):
    #add code here
    if len(l)%2>0:
        l.pop()
    i = 0
    stack = []
    while i<len(l)-1:
        stack.append(l[i])
        if abs(l[i+1] - stack[-1]) != 1:
            return False
        else:
            stack.pop()
        i +=2
    return True
