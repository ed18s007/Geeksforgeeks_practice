#code
for T in range(int(input())):
    N = int(input())
    arr = [map(int, input().split())]
    k = int(input())
    arr.sort()
    print(arr[k-1])