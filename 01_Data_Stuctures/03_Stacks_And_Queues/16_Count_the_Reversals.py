 # Count the Reversals 
#code
import math
for T in range(int(input())):
    exp = input()
    if len(exp)%2 >0:
        print(-1)
        continue
    stack = []
    count = 0
    ini = 0
    for char in exp:
        if not stack:
            if char == "}":
                ini+=1
            else:
                stack.append(char)
        else:
            if char == "{":
                stack.append(char)
            else:
                stack.pop()
    fin = 0
    while stack:
        fin +=1
        stack.pop()
    print(int(math.ceil(ini/2)+math.ceil(fin/2)+count))