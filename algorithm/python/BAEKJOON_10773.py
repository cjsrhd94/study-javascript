case = int(input())

sum_list = []
for i in range(case):
    number = int(input())
    if number == 0:
        sum_list.pop()
    else:
        sum_list.append(number)



print(sum(sum_list))