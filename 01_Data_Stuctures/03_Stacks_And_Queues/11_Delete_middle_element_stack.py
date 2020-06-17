 Delete middle element of a stack 
import math
##Complete this function
def deleteMid(s, sizeOfStack, current):
    ##Your code here
    s.pop(int(math.ceil(sizeOfStack-1)/2))
    return s
