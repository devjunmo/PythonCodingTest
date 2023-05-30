"""
6 5
1 2
2 5
5 1
3 4
4 6
"""

import sys
input=sys.stdin.readline
N, M = list(map(int, input().split(" ")))
adj_lst = []
vis_lst = [False] * (N+1)


for i in range(N+1):
    adj_lst.append([])

for _ in range(M):
    st, ed = list(map(int, input().split(" ")))
    adj_lst[st].append(ed)
    adj_lst[ed].append(st)

res = 0

from collections import deque


def bfs(st):
    dq = deque([st])
    vis_lst[st] = True
    while dq:
        cur_point = dq.pop()
        adj_point_lst = adj_lst[cur_point]
        for nxt_point in adj_point_lst:
            # 방문 안했을 때만
            if not vis_lst[nxt_point]:
                vis_lst[nxt_point] = True
                dq.appendleft(nxt_point)


# 1부터 N까지 모든 정점에 대해 시작 점으로 하여 bfs 진행 시키기. bfs 진행 하면 res++
for i in range(1, N+1):
    if not vis_lst[i]:
        bfs(i)
        res += 1

print(res)