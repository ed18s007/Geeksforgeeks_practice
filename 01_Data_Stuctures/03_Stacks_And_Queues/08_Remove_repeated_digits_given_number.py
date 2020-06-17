 # Remove repeated digits in a given number 
 #code
for T in range(int(input())):
    stack = []
    N = input()
    for char in N:
        if not stack:
            stack.append(char)
        elif stack[-1] == char:
            continue
        else:
            stack.append(char)
    print(''.join(stack))
            