def reverse(string):
    
    #Add code here
    stack = []
    for i in string:
        stack.append(i)
    rev_string = ''
    while stack:
        rev_string += str(stack.pop())
    return rev_string
