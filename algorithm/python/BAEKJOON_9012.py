case = int(input())
for i in range(case):
    stack = []
    vps = input()
    check = 0
    for j in vps:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if len(stack) == 0:
                print('NO')
                check += 1
                break
            else:
                stack.pop(-1)

    if len(stack) != 0 and check == 0:
        print('NO')
    elif len(stack) == 0 and check == 0:
        print('YES')