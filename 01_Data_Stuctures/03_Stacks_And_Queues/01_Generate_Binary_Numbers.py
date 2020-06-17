 Generate Binary Numbers 
#code
for T in range(int(input())):
    N = int(input())
    queue = ["1"]
    i = 0
    while i<N:
        val = queue.pop(0)
        i+=1
        print(val,end=" ")
        queue.append(val+"0")
        queue.append(val+"1")
    print()