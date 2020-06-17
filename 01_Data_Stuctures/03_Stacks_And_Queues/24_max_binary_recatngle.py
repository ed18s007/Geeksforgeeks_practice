#User function Template for python3
def max_row_area(arr):
    stack = []
    max_area = 0
    i = 0
    while i<len(arr):
        if (not stack) or arr[stack[-1]]<=arr[i]:
            stack.append(i)
            i+=1
        else:
            left = stack.pop()
            area = arr[left]*(i if not stack else (i-stack[-1]-1))
            max_area = max(max_area,area)
    while stack:
        left = stack.pop()
        area = arr[left]*(i if not stack else (i-stack[-1]-1))
        max_area = max(area, max_area)
    return max_area

def maxRectangle(A, R, C):
    # code here
    max_area = 0
    row = [0]*C
    for i in range(R):
        for j in range(C):
            row[j] = row[j]+A[i][j] if (A[i][j]>0) else 0
        # print(i,row,max_row_area(row))
        max_area = max(max_area,max_row_area(row))
    return max_area


#{ 
#  Driver Code Starts
#Initial Template for Python 3



# Driver Code 
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        R, C = input().split()
        a=list(map(int,input().split()))
        j=0
        A=[]
        R=int(R)
        C=int(C)
        for i in range(0,R):
            A.append(a[j:j+C])
            j=j+C
        # print(A)
        print(maxRectangle(A, R, C)) 
	
# This code is contributed 
# by SHUBHAMSINGH10 

# } Driver Code Ends