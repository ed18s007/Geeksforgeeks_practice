 # Reverse First K elements of Queue 
'''
Function Arguments :
		@param  : queue ( given queue to be used), k(Integer ),n(size of queue)
		@return : lsit, just reverse the first k elements of queue and return new queue
'''

def reverseK(queue,k,n):
    # code here
    rev_k = []
    for i in range(k):
        rev_k.append(queue[k-i-1])
    return rev_k + queue[k:]
    # k_q = queue[:k]
    # return k_q[::-1]+queue[k:]
