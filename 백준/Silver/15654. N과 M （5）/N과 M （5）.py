
N, M = list(map(int, input().split(" ")))

input_lst = list(map(int, input().split(" ")))

from itertools import permutations

comb = permutations(input_lst, M)

res_lst = []

for c in comb:
    res_lst.append(list(c))

res_lst = sorted(res_lst, key=tuple)

for r in res_lst:
    print(*r)