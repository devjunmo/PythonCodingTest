case_num = 10

MAX_H = 255


def check_view(arr, in_len):

    global view_cnt

    for i in range(in_len):
        for j in range(MAX_H):
            if arr[i][j] == 0:
                continue
            else:
                try:
                    val1 = arr[i - 2][j]
                    val2 = arr[i - 1][j]
                    val3 = arr[i + 1][j]
                    val4 = arr[i + 2][j]

                    if val1 + val2 + val3 + val4 == 0:
                        view_cnt += 1

                except IndexError:
                    continue


for c_num in range(1, case_num+1):

    input_len = int(input())
    my_arr = [[0]] * input_len
    num_lst = list(map(int, input().split()))
    view_cnt = 0

    for i in range(len(num_lst)):

        cur_num = num_lst[i]
        zero_num = MAX_H - cur_num

        if cur_num == 0:
            my_arr[i] = [0] * MAX_H
            continue

        my_arr[i] = ([1] * cur_num) + ([0] * zero_num)

    check_view(my_arr, input_len)
    print(f'#{c_num} {view_cnt}')





