def reverseK(queue,k,n):
    # code here
    k_q = queue[:k]
    return k_q[::-1]+queue[k:]

def reverseK(queue,k,n):
    # code here
    rev_k = []
    for i in range(k):
        rev_k.append(queue[k-i-1])
    return rev_k + queue[k:]