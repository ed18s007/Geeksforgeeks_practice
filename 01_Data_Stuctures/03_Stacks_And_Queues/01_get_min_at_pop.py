#User function Template for python3

def _push(a,n):
    '''
    :param a: given array
    :param n: given size of array
    :return: stack
    '''
    # code here
    stack = []
    for i in range(n):
        stack.append(a[i])
    return stack
    
def _getMinAtPop(stack):
    '''
    :param stack: our stack
    :return: none, print the elements in order of pop one by one, new line is not required
    '''
    # code here
    min_dict = {}
    min_stck = float('inf')
    n = len(stack)
    min_ls = []
    for i in range(n):
        if stack[i] < min_stck:
            min_ls.append(stack[i])
            min_dict[i] = stack[i]
            min_stck = stack[i]

    min_stck = min_ls.pop()
    for j in range(n-1, -1, -1):
        if j in min_dict:
            print(min_stck,end=" ")
            if len(min_ls)>0:
                min_stck = min_ls.pop()
        else:
            print(min_stck,end=" ")
        stack.pop()

    return None
