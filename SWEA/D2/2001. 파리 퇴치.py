case_num = int(input())

for c_num in range(case_num):
    print_num = c_num + 1
    n, m = list(map(int, input().split()))  # 3, 2
    fly_lst = []

    for _ in range(n):
        fly_lst.append(list(map(int, input().split())))

    start_row = 0
    start_col = 0

    sum_lst = []

    while True:
        try:
            if start_col + m - 1 <= n - 1:
                fly_count_lst = []
                for i in range(m):
                    for j in range(m):
                        tmp_val = fly_lst[start_row+i][start_col+j]
                        fly_count_lst.append(tmp_val)
                sum_lst.append(sum(fly_count_lst))

            else:
                start_col = 0
                start_row += 1

        except IndexError:
            fly_count_lst = []
            break

        start_col += 1

    max_val = max(sum_lst)

    print(f'#{print_num} {max_val}')

