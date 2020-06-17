 # Maximum of minimum for every window size 
 #code
for T in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    out = []
    out.append(min(arr))
    min_arr = [0]*N 
    pt1,pt2 = 0,1
    min_arr[0] = max(arr)
    i,k = 1,1
    while pt1<N:
        while pt2<N:
            min_arr[i] = max(min_arr[i],min(arr[pt1:pt2+1]))
            i+=1
            pt2+=1
        i=k
        # print(pt1,pt2,min_arr)
        pt1+=1
        pt2=pt1+1
    print(*min_arr,sep=" ")

