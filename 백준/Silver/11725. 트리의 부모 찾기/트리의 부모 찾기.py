"""
7
1 6
6 3
3 5
4 1
2 4
4 7
"""

import sys
from collections import deque

adj_lst = [[]]

N = int(input())

for _ in range(N):
    adj_lst.append([])

parent_lst = [0] * (N+1)

for _ in range(N-1):
    ij = sys.stdin.readline().split(" ")
    i = int(ij[0])
    j = int(ij[1])
    
    adj_lst[i].append(j)
    adj_lst[j].append(i)


# 1부터 레벨순회

dq = deque([1])
parent_lst[1] = -1 # 방문 체크용으로

while dq:
    cur_v = dq.pop()
    child_v_lst = adj_lst[cur_v]
    
    # 자식들에 대해 부모 배열 채우기
    for cv in child_v_lst:
        # 부모가 기록 되지 않았을때만
        if parent_lst[cv] == 0:
            parent_lst[cv] = cur_v
            dq.appendleft(cv)

for i in range(2, N+1):
    print(parent_lst[i])
    
    
    
    