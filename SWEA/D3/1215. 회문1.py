case_num = 10
arr_len = 8

def is_hm(lst):
    res = []
    fst_str = "".join(lst)
    for _ in range(len(lst)):
        res.append(lst.pop())
    res_str = "".join(res)

    if fst_str == res_str:
        return True
    else:
        return False


for c_num in range(1, case_num + 1):
    window_size = int(input())
    arr_2x = [list(input()) for _ in range(arr_len)]
    t_arr = list(map(list, zip(*arr_2x)))

    ans = 0

    for i in range(arr_len):
        for j in range(arr_len):
            try:
                if j+window_size > arr_len:
                    break
                cur_lst = arr_2x[i][j:j+window_size]
                if is_hm(cur_lst):
                    ans += 1

            except IndexError:
                break

    for i in range(arr_len):
        for j in range(arr_len):
            try:
                if j+window_size > arr_len:
                    break
                cur_lst = t_arr[i][j:j+window_size]
                if is_hm(cur_lst):
                    ans += 1

            except IndexError:
                break

    print(f'#{c_num} {ans}')