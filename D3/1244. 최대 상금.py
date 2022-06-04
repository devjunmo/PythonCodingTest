# case_num = int(input())
#
#
# def swap(lst, j, k):
#     tmp_lst = lst.copy()
#     tmp_val = tmp_lst[j]
#     tmp_lst[j] = tmp_lst[k]
#     tmp_lst[k] = tmp_val
#
#     return int("".join(tmp_lst))
#
#
# def processing(cur_lst):
#     global cur_cnt
#     cur_tmp_lst = []
#
#     for i in range(len(cur_lst)):
#         cur_val = cur_lst[i] # 123
#         cur_val_lst = list(str(cur_val)) # 1, 2, 3
#         # print(cur_val_lst)
#         for j in range(len(cur_val_lst)):
#             for k in range(j+1, len(cur_val_lst)):
#                 cur_tmp_lst.append(swap(cur_val_lst, j, k))
#
#     cur_cnt += 1
#
#     if cur_cnt == loop_num:
#         cur_cnt = 0
#         return cur_tmp_lst
#
#     try:
#         return processing(cur_tmp_lst)
#     except Exception:
#         return [max(processing(cur_tmp_lst[:len(cur_tmp_lst)/2]))] + [max(processing(cur_tmp_lst[len(cur_tmp_lst)/2:]))]
#
#
#
# for c_num in range(1, case_num+1):
#
#     input_lst = input().split()
#
#     input_num = int(input_lst[0])
#     loop_num = int(input_lst[1])
#
#     cur_input_lst = [input_num]
#
#     cur_cnt = 0
#     ans_num_lst = processing(cur_input_lst)
#     # print(ans_num_lst)
#     print(f'#{c_num} {max(ans_num_lst)}')
"""
최대 상금 2트 -> 220525
"""
case_num = int(input())


def dfs(count):
    global max_val

    if count == change_num:
        if max_val == 0:
            max_val = int("".join(map(str, input_lst)))

        elif 0 < max_val < int("".join(map(str, input_lst))):
            max_val = int("".join(map(str, input_lst)))
        return

    for i in range(lst_len - 1):
        for j in range(i+1, lst_len):
            input_lst[i], input_lst[j] = input_lst[j], input_lst[i]

            tmp_val = int("".join(map(str, input_lst)))
            if vis.get((count+1, tmp_val), True):
                vis[(count+1, tmp_val)] = False
                dfs(count + 1)
            input_lst[j], input_lst[i] = input_lst[i], input_lst[j]


for c_num in range(1, case_num+1):

    max_val = 0

    lst_num, change_num = map(int, input().split())

    input_lst = list(map(int, list(str(lst_num))))
    lst_len = len(input_lst)

    vis = dict()

    dfs(0)

    print(f'#{c_num} {max_val}')
