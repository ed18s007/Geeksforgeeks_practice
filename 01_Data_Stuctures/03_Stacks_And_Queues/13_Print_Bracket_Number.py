 # Print Bracket Number 
for T in range(int(input())):
    exp = input()
    prnt = []
    stack = []
    count = 1
    for char in exp:
        if char=="(":
            stack.append(count)
            prnt.append(count)
            count+=1
        elif char==")":
            if stack:
                val = stack.pop()
                prnt.append(val)
    print(*prnt,sep=" ")