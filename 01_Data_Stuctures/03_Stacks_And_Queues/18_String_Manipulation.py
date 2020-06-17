 # String Manipulation 
 #code
for T in range(int(input())):
    N = int(input())
    seq = input().split()
    stack = []
    for wrd in seq:
        if not stack:
            stack.append(wrd)
        else:
            if stack[-1]==wrd:
                stack.pop()
            else:
                stack.append(wrd)
    print(len(stack))