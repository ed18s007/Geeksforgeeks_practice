 # Chinky and diamonds 
 #code
for T in range(int(input())):
    N, K = map(int, input().split())
    arr = list(map(int,input().split()))
    cnt = 0
    for i in range(K):
        curr = max(arr)
        idx = arr.index(curr)
        cnt+=curr
        curr = curr//2
        arr[idx]=curr
    print(cnt)
            
        
        
    