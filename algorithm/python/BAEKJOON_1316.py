case = int(input())

answer = 0

for i in range(case):
    letter = input().lower()
    letter_list = list(set(letter))
    count_list = []

    for j in letter_list:
        count = letter.count(j)
        count_list.append(count)

    check_count = 0
    for k in range(len(letter_list)):
        checker = letter_list[k] * count_list[k]
        if checker in letter:
            check_count += 1
    if check_count == len(letter_list):
        answer += 1

print(answer)