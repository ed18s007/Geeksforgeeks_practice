Save Gotham
#code
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