"""
10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10
"""

import sys

input = sys.stdin.readline

N = int(input())
N_lst = list(map(int, input().split(" ")))
N_lst.sort()

M = int(input())
M_lst = list(map(int, input().split(" ")))

from bisect import bisect_left,bisect_right

res = []
for m in M_lst:
    l_idx = bisect_left(N_lst, m)
    r_idx = bisect_right(N_lst, m)
    idx_gap = r_idx-l_idx
    res.append(idx_gap)

print(*res)