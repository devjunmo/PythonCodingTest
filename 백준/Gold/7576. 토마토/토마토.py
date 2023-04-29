"""
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
"""

MN = list(map(int, input().split(" ")))
M = MN[0]
N = MN[1]

# 상우하좌 
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

input_lst = []
dist_lst = []

for _ in range(N):
    input_lst.append(list(map(int, input().split(" "))))

import sys

# 모두 익어있는 상태면 0 출력
def check_all_one():
    zero_cnt = 0
    for i in range(N):
        for j in range(M):
            if input_lst[i][j] == 0:
                zero_cnt += 1
    if zero_cnt == 0:
        print(0)
        sys.exit()

check_all_one()

# dist lst 채우기
for _ in range(N):
    dist_lst.append([-1] * M)


from collections import deque

# bfs 시작점 리스트 만들기
start_point_lst = []
for i in range(N):
    for j in range(M):
        if input_lst[i][j] == 1:
            start_point_lst.append((i, j))


def bfs(st_lst):
    # 시작점들을 덱에 넣고 시작
    dq = deque(st_lst)
    # print(dq)
    
    for st_tup in dq:
        # 현 위치 거리 = 영
        dist_lst[st_tup[0]][st_tup[1]] = 0

    while len(dq) != 0:
        cur_point = dq.pop()
        
        # 4방탐색
        for i in range(4):
            nxt_x = cur_point[0] + dx[i]
            nxt_y = cur_point[1] + dy[i]
            
            # 정상범위 이면서 안익은 토마토일때 
            if 0<=nxt_x<N and 0<=nxt_y<M and input_lst[nxt_x][nxt_y] == 0 and dist_lst[nxt_x][nxt_y] == -1:
                # dist 배열 채우고 next point 큐에 넣기
                dist_lst[nxt_x][nxt_y] = dist_lst[cur_point[0]][cur_point[1]] + 1
                dq.appendleft((nxt_x, nxt_y))

bfs(start_point_lst)

# print(dist_lst)

# input_lst의 -1이 있던 자리 제외하고 모두 익지 못하는 상태면 -1 출력 
def check_not_ripe():
    zero_cnt = 0
    for i in range(N):
        for j in range(M):
            if input_lst[i][j] != -1 and dist_lst[i][j] == -1:
                zero_cnt += 1
    if zero_cnt != 0:
        print(-1)
        sys.exit()

check_not_ripe()

max_val = -100
for i in range(N):
    for j in range(M):
        if dist_lst[i][j] > max_val:
            max_val = dist_lst[i][j]

print(max_val)