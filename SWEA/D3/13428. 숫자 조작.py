case_num = int(input())



def swap(lst, target1, target2):
    tmp_lst = lst.copy()
    if target1 == 0 and tmp_lst[target2] == 0:
        return -1
    tmp = tmp_lst[target1]
    tmp_lst[target1] = tmp_lst[target2]
    tmp_lst[target2] = tmp

    res.append(int("".join(map(str, tmp_lst))))


for c_num in range(1, case_num+1):

    res = []
    input_str = input()
    input_lst = list(map(int, list(input_str)))
    # print(input_lst)

    res.append(int(input_str))

    for i in range(len(input_lst)):
        for j in range(i+1, len(input_lst)):
            swap(input_lst, i, j)

    ans = [ans for ans in res if ans != -1]

    print(f'#{c_num} {min(ans)} {max(ans)}')
