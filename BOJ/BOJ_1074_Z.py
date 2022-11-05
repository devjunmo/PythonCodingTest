import sys

"""
시간 or 메모리 극복 방안 
다 돌면서 cnt 갱신 하지 말고
인덱스로 내 목표 rc가 있는지 판단하고 없으면 pass하도록 고쳐보기 
"""

N, r, c = list(map(int, input().split(" ")))

cnt = 0

N = 2**N


def div(start_row, start_col, cur_len):
    global cnt

    if cur_len == 1:
        print(int(cnt))
        return

    half_len = cur_len/2

    # 좌상
    if (start_row <= r <= start_row + half_len - 1) and (start_col <= c <= start_col + half_len - 1):
        div(start_row, start_col, half_len)

    # 우상
    elif (start_row <= r <= start_row + half_len - 1) and (start_col + half_len <= c <= start_col + cur_len - 1):
        cnt += half_len * half_len
        div(start_row, start_col + half_len, half_len)

    # 좌하
    elif (start_row + half_len <= r <= start_row + cur_len - 1) and (start_col <= c <= start_col + half_len - 1):
        cnt += 2 * half_len * half_len
        div(start_row + half_len, start_col, half_len)

    # 우하
    elif (start_row + half_len <= r <= start_row + cur_len - 1) and (start_col + half_len <= c <= start_col + cur_len - 1):
        cnt += 3 * half_len * half_len
        div(start_row + half_len, start_col + half_len, half_len)


div(0, 0, N)
