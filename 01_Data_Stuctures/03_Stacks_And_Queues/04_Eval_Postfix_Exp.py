for T in range(int(input())):
    arr = input()
    stack = []
    for char in arr:
        if char in ['+', '-', '*', '/']:
            a = stack.pop()
            b = stack.pop()
            val = str(int(eval(b+char+a)))
            stack.append(val)
        else:
            stack.append(char)
    print(stack.pop())
        