#code
for T in range(int(input())):
    N = int(input())
    arr2 = [0]*N
    arr = list(map(int, input().split()))
    for i in range(N):
        idx = arr[i] - 1
        arr2[idx] = i + 1
    print(*arr2, sep=" ")