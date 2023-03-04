case_num = int(input())
# case_num = 1

for c_num in range(1, case_num+1):

    input_lst = list(input())
    # input_lst = list('oxoxoxoxoxoxoxo')
    # print(input_lst)

    o_cnt = input_lst.count('o')
    lst_ln = len(input_lst)
    remains = 15 - lst_ln

    ans = ''

    if o_cnt + remains >= 8:
        ans = "YES"
    else:
        ans = "NO"

    print(f'#{c_num} {ans}')


