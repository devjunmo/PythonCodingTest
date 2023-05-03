
"""
4 4
####
#JF#
#..#
#..#
"""
# IMPOSSIBLE


NM = list(map(int, input().split(" ")))
N = NM[0]
M = NM[1]

input_arr = []
init_comp_lst = [] # 처음 지훈, 불 위치정보

# 상우하좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

import sys


# J일 때 탈출 조건인지 체크
def check_exit(custom_tup):
    x = custom_tup[2][0]
    y = custom_tup[2][1]
    # 가장자리면
    if x == 0 or x == N or y == 0 or y ==M:
        print(custom_tup[1])
        sys.exit()


jh_st = (-1,-1)
fire_st_lst = []


for i in range(N):
    tmp_lst = []
    tmp_row = input()
    for j in range(len(tmp_row)):
        s = tmp_row[j]
        tmp_lst.append(s)
        if s == 'J':
            jh_st = (i, j)
        elif s == 'F':
            fire_st_lst.append((i, j))
            
    input_arr.append(tmp_lst)   

# print(input_arr)


from collections import deque


fire_dist_lst = []

for _ in range(N):
    fire_dist_lst.append([10000001] * M)


# 불의 dist배열 먼저 만든다음, 지훈이 bfs 탈 때 dist보다 작은곳으로만 갈 수 있도록 한다 
def bfs_fire():
    dq = deque(fire_st_lst)
    for pnt in dq:
        x = pnt[0]
        y = pnt[1]
        fire_dist_lst[x][y] = 0 # 현재 위치 영
    
    while(len(dq) != 0):
        cur_point = dq.pop()
        x = cur_point[0]
        y = cur_point[1]

        # 4방 탐색 
        for i in range(4):
            nx = cur_point[0] + dx[i]
            ny = cur_point[1] + dy[i]
            
            # 정상범위 이면서 안간곳이면서 . 또는 J
            if 0<=nx<N and 0<=ny<M and fire_dist_lst[nx][ny] == 10000001 and (input_arr[nx][ny] == '.' or input_arr[nx][ny] == 'J'):
                dq.appendleft((nx,ny))
                fire_dist_lst[nx][ny] = fire_dist_lst[x][y] + 1

bfs_fire()

# print(fire_dist_lst)


jh_dist_lst = []

for _ in range(N):
    jh_dist_lst.append([10000001] * M)
    

def bfs_jh():
    dq = deque([jh_st])
    for pnt in dq:
        x = pnt[0]
        y = pnt[1]
        jh_dist_lst[x][y] = 0 # 현재 위치 영
    
    
    while(len(dq) != 0):
        cur_point = dq.pop()
        x = cur_point[0]
        y = cur_point[1]
        # 가장자리면
        # print(x,y)
        if x == 0 or x == N-1 or y == 0 or y == M-1:
            print(jh_dist_lst[x][y] + 1)
            sys.exit()

        # 4방 탐색 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 정상범위 이면서 안간곳이면서 .
            if 0<=nx<N and 0<=ny<M and jh_dist_lst[nx][ny] == 10000001 and input_arr[nx][ny] == '.':
                # nxt로 갈 곳의 거리가 불의 거리보다 작아야됨
                if (jh_dist_lst[x][y] + 1) < fire_dist_lst[nx][ny]: 
                    dq.appendleft((nx,ny))
                    jh_dist_lst[nx][ny] = jh_dist_lst[x][y] + 1
                    

bfs_jh()
print("IMPOSSIBLE")