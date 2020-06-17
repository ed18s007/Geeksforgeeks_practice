 # Infix to Postfix 
 #code
def priority(char):
    if char=="+" or char=="-":
        return 1
    elif char=="*" or char=="/":
        return 2
    elif char=="^":
        return 3
    return 0

for T in range(int(input())):
    exp = input()
    stack = []
    output = []
    for c in exp:
        if c=="(":
            stack.append(c)
        elif c==")":
            while stack[-1] is not "(":
                output.append(stack.pop())
            stack.pop()
        elif priority(c)==0:
            output.append(c)
        else:
            p = priority(c)
            if not stack:
                stack.append(c)
            elif p> priority(stack[-1]):
                stack.append(c)
            else:
                while p <= priority(stack[-1]):
                    output.append(stack.pop())
                    if not stack:
                        break
                stack.append(c)
    while stack:
        output.append(stack.pop())
    print(*output,sep="")
        