 The Celebrity Problem 
#User function Template for python3
'''
Function Arguments :
		@param  :m (boolean matrix of size n*n), n(no of rows and cols )
		@return : Integer
'''
def getId(m,n):
    # code here
    for i in range(n):
        row = sum(m[i])
        if row==0:
            for j in range(n):
                if (m[j][i] == 1) or (i==j):
                    continue
                else:
                    j=-1
                    break
            if j==n-1:
                return i
    return -1



#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

#Contributed by :Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        k = 0
        m = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(a[k])
                k+=1
            m.append(row)
        print(getId(m,n))
# } Driver Code Ends