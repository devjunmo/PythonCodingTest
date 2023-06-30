
from collections import defaultdict

N, M = list(map(int, input().split(" ")))
input_lst = list(map(int, input().split(" ")))

input_lst.sort()
res_lst = []
vis_dict = defaultdict(bool)
vis_num = [False] * N


def dfs():
    if len(res_lst) == M:
        res_tup = tuple(res_lst)
        if vis_dict[res_tup]:
            return
        else:
            print(*res_lst)
            vis_dict[res_tup] = True
            return

    for i in range(N):
        if not vis_num[i]:
            vis_num[i] = True
            res_lst.append(input_lst[i])
            dfs()
            vis_num[i] = False
            res_lst.pop()


dfs()
