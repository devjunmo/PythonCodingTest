"""
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
고른 수열은 오름차순이어야 한다.
"""

from itertools import combinations
from collections import defaultdict

N, M = list(map(int, input().split(" ")))

input_lst = [x for x in range(1, N+1)]
res_dict = defaultdict(bool)
res_lst = []

combs = combinations(input_lst, M)

for comb in combs:
    lcomb = list(comb)
    lcomb.sort()
    tcomb = tuple(lcomb)
    if not res_dict[tcomb]:
        res_dict[tcomb] = True
        res_lst.append(lcomb)

for r in res_lst:
    print(*r)
