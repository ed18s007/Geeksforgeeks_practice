 # Smallest number on left 
 #code
for T in range(int(input())):
    N = int(input())
    stack = []
    arr = list(map(int, input().split()))
    sml = [-1]*N
    i=N-1
    while i>-1:
        if not stack:
            stack.append(i)
        else:
            if arr[i]<arr[stack[-1]]:
                while arr[i]<arr[stack[-1]]:
                    sml[stack[-1]] = arr[i]
                    stack.pop()
                    if not stack:
                        break
                stack.append(i)
            else:
                stack.append(i)
        i-=1
    print(*sml,sep=" ")