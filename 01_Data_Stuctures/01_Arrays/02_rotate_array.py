#code
for T in range(int(input())):
    N, D = map(int, input().split())
    arr = list(map(int, input().split()))
    print(*(arr[D:] + arr[:D]), sep=" ")