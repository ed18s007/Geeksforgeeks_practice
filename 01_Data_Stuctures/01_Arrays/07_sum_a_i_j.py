for T in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    sum = 0
    for i in range(N):
        for j in range(i+1, N):
            if abs(arr[j] - arr[i])>1:
                sum += arr[j] - arr[i]
    print(sum)