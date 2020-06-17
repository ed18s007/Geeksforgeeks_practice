 # Parenthesis Checker 
 #code
def brace_num(br):
    if br==")":
        return 0
    elif br=="]":
        return 1
    else:
        return 2
        
for T in range(int(input())):
    exp = input()
    stack = []
    open_br = ["(","[","{"]
    close_br = [")","]","}"]
    char = "continue"
    for c in exp:
        if not stack:
            stack.append(c)
        else:
            if c in open_br:
                stack.append(c)
            else:
                if stack[-1]==open_br[brace_num(c)]:
                    stack.pop()
                else:
                    char = "break"
        if char=="break":
            break
    if not stack:
        print("balanced")
    else:
        print("not balanced")
                