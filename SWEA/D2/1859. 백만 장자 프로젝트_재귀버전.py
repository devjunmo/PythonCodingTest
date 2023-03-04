case_num = int(input())


def processing_left(p_left):
    global my_profit
    max_tmp = p_left[-1]
    profit_list_left = [max_tmp - i for i in p_left[:len(p_left) - 1]]
    my_profit += sum(profit_list_left)


def price_recur(price_lst):
    max_idx = price_lst.index(max(price_lst))
    p_left = price_lst[:max_idx + 1]
    p_right = price_lst[max_idx + 1:]
    processing_left(p_left)

    if len(p_right) == 0:
        return 0

    price_recur(p_right)


for c_num in range(1, case_num+1):

    input_len = int(input())
    price_lst = list(map(int, input().split()))

    my_profit = 0
    price_recur(price_lst)
    print(f'#{c_num} {my_profit}')










