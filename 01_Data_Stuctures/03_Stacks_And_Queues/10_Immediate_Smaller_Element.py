 # Immediate Smaller Element 
 #code
for T in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    stack = []
    stack.append(float("inf"))
    for i in range(N):
        if arr[i]<stack[-1]:
            print(arr[i],end=" ")
        else:
            print(-1,end=" ")
        stack.append(arr[i])
    print(-1)