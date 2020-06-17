# code NAIVE
for T in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    max_area = arr[0]
    for i in range(1,N):
        stack = arr[:i+1]
        for j in range(i+1):
            min_area = (len(stack[j:]))*min(stack[j:])
            if min_area > max_area:
                    max_area = min_area
    print(max_area)  
    
for T in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    stack = []
    max_area = 0
    i = 0
    while i<N:
        if (not stack) or (arr[stack[-1]]<=arr[i]):
            stack.append(i)
            i+=1
        else:
            left = stack.pop()
            area = arr[left]*((i-stack[-1]-1) if stack else i)
            max_area = max(area,max_area)
    while stack:
        left = stack.pop()
        area = arr[left]*((i-stack[-1]-1) if stack else i)
        max_area = max(area,max_area)
    print(max_area)        
# Python3 program to find maximum 
# rectangular area in linear time 

def max_area_histogram(histogram): 
    
    # This function calulates maximum 
    # rectangular area under given 
    # histogram with n bars 

    # Create an empty stack. The stack 
    # holds indexes of histogram[] list. 
    # The bars stored in the stack are 
    # always in increasing order of 
    # their heights. 
    stack = list() 

    max_area = 0 # Initialize max area 

    # Run through all bars of 
    # given histogram 
    index = 0
    while index < len(histogram): 
        print(stack)
        
        # If this bar is higher 
        # than the bar on top 
        # stack, push it to stack 

        if (not stack) or (histogram[stack[-1]] <= histogram[index]): 
            stack.append(index) 
            index += 1

        # If this bar is lower than top of stack, 
        # then calculate area of rectangle with 
        # stack top as the smallest (or minimum 
        # height) bar.'i' is 'right index' for 
        # the top and element before top in stack 
        # is 'left index' 
        else: 
            # pop the top 
            top_of_stack = stack.pop() 

            # Calculate the area with 
            # histogram[top_of_stack] stack 
            # as smallest bar 
            area = (histogram[top_of_stack] *
                ((index - stack[-1] - 1) 
                if stack else index)) 

            # update max area, if needed 
            max_area = max(max_area, area) 

    # Now pop the remaining bars from 
    # stack and calculate area with 
    # every popped bar as the smallest bar 
    while stack: 
        print("now",stack)
        
        # pop the top 
        top_of_stack = stack.pop() 

        # Calculate the area with 
        # histogram[top_of_stack] 
        # stack as smallest bar 
        area = (histogram[top_of_stack] *
            ((index - stack[-1] - 1) 
                if stack else index)) 

        # update max area, if needed 
        max_area = max(max_area, area) 

    # Return maximum area under 
    # the given histogram 
    return max_area 

# Driver Code 
hist = [6, 2, 5, 4, 5, 1, 6] 
print("here")
print("Maximum area is", max_area_histogram(hist)) 

# This code is contributed 
# by Jinay Shah 
