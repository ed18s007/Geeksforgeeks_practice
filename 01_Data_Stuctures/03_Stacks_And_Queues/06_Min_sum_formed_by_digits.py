 Min sum formed by digits 
#code
for T in range(int(input())):
    N = int(input())
    exp = input().replace(" ", "") 
    ls = sorted(exp)
    num1, num2 = "", ""
    pt1, pt2 = 0,1
    while pt1<N:
        num1+=ls[pt1]
        pt1+=2
    while pt2<N:
        num2+=ls[pt2]
        pt2+=2
    print(int(num1)+ int(num2))

        