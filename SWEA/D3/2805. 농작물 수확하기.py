from collections import deque

case_num = int(input())

for c_num in range(1, case_num + 1):
    f_size = int(input())
    arr_2x = [list(map(int, input())) for _ in range(f_size)]
    ans = []
    mid_idx = int((f_size - 1) / 2)
    ref_dq = deque([i for i in range(f_size)])

    for i in range(f_size):
        tmp_dq = ref_dq.copy()
        pad_cnt = abs(i - mid_idx)

        for _ in range(pad_cnt):
            tmp_dq.pop()
            tmp_dq.popleft()

        for k in list(tmp_dq):
            ans.append(arr_2x[i][k])

    print(f'#{c_num} {sum(ans)}')
