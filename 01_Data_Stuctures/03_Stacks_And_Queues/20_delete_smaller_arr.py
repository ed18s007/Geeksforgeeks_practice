 # Delete array elements which are smaller than next or become smaller
 #code
for T in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    stack = [arr[0]]
    i = 1
    while k>0:
        if not stack:
            stack.append(arr[i])
            i+=1
        if i>=N:
            break
        if stack[-1] < arr[i]:
            stack.pop()
            k-=1
        else:
            stack.append(arr[i])
            i+=1
    stack = stack +arr[i:]
    print(*stack,sep=" ")
        