for T in range(int(input())):
    N = int(input())
    ls = [0]*N
    inp_arr = list(map(int, input().split()))
    for i in range(N):
        elem = inp_arr[i]
        for j in range(N):
            curr = inp_arr[j]
            if curr>elem:
                ls[j] +=1
            elif curr<elem:
                ls[i] += 1
    ls = [x//2 for x in ls]           
    print(*ls,sep=" ")
