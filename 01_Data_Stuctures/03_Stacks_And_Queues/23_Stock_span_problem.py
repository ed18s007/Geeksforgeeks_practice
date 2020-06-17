 # Stock span problem 
 #code
for T in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    stack = []
    consec = [1]*N
    i=N-1;
    while i>-1:
        if not stack:
            stack.append(i)
        else:
            if arr[stack[-1]]<arr[i]:
                while arr[stack[-1]]<arr[i]:
                    consec[stack[-1]] = stack[-1]-i
                    stack.pop()
                    if not stack:
                        break
                stack.append(i)
            else:
                stack.append(i)
        i-=1
    while stack:
        consec[stack[-1]]=stack[-1]+1
        stack.pop()
    print(*consec,sep=" ")