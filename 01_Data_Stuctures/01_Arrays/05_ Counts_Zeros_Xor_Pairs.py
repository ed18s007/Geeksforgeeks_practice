#code
for T in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        a = arr[i]
        for j in range(i+1, N):
            b = arr[j]
            if a^b == 0:
                cnt += 1
    print(cnt)
    