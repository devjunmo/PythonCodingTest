case_num = int(input())


for c_num in range(1, case_num+1):

    input_len = int(input())

    price_lst = list(map(int, input().split()))

    my_profit = 0

    while True:

        if len(price_lst) == 0:
            break

        max_idx = price_lst.index(max(price_lst))

        p_left = price_lst[:max_idx+1]
        price_lst = price_lst[max_idx+1:]  # right.  right의 len이 영이라면 while문 break이 가능

        # left에 대해 처리 해주기
        # process_tst = [max_tmp - i for i in max_tst[:len(max_tst)-1]]
        # [1 3 5 7]
        max_tmp = p_left[-1]
        profit_list_left = [max_tmp - i for i in p_left[:len(p_left)-1]]
        my_profit += sum(profit_list_left)

    print(f'#{c_num} {my_profit}')





