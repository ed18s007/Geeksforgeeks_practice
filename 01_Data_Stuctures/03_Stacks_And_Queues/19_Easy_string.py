 Easy string 
#code
for T in range(int(input())):
    exp = input()
    exp = exp.lower()
    cnt = 1
    s = exp[0]
    ans = ""
    for i in range(1,len(exp)):
        if exp[i]==s:
            cnt +=1
        else:
            ans += str(cnt) + s
            cnt = 1
            s = exp[i]
    ans += str(cnt) + s
    print(ans)