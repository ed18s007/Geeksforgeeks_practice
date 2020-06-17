 # Next larger element 
 #code
#code
for T in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    stack,stack2 = [],[]
    left = [-1]*N
    right = [N]*N
    i = N-1
    while i>-1:
        if (not stack) or arr[i]>=arr[stack[-1]]:
            stack.append(i)
            i-=1
        else:
            left[stack[-1]] = i
            stack.pop()
    i = 0
    while i<N:
        if (not stack2) or arr[i]>=arr[stack2[-1]]:
            stack2.append(i)
            i+=1
        else:
            right[stack2[-1]] = i
            stack2.pop()
    ans = [0]*(N+1) 
    for i in range(N):
        leng = right[i]-left[i]-1
        ans[leng] = max(ans[leng],arr[i])
    for i in range(N-1,-1,-1):
        ans[i] = max(ans[i],ans[i+1])
    ans = ans[1:]
    print(*ans,sep=" ")

   
 
for T in range(int(input())):
    N = int(input())
    arr = list(map(int,input().split()))
    stack = []
    out = [-1]*N
    i = 0
    while i<N:
        if (not stack) or (arr[i]<=arr[stack[-1]]):
            stack.append(i)
            i+=1
        else:
            left = stack.pop()
            out[left] = arr[i]
    print(*out,sep=" ")