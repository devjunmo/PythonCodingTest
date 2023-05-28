import sys
from collections import deque
from pprint import pprint

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    M, N, K = list(map(int, input().split(" ")))
    # 상우하좌
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    input_map = []
    vis_map = []

    for i in range(N):
        input_map.append([0] * M)
        vis_map.append([False] * M)

    for _ in range(K):
        # col, row 순으로 줌 
        Y, X = list(map(int, input().split(" ")))
        input_map[X][Y] = 1

    res = 0

    # 모든 포인트를 시작점으로 bfs 진행 
    for i in range(N):
        for j in range(M):
            if input_map[i][j] == 1 and vis_map[i][j] == False:
                res += 1 # 필요 지렁이 수 증가
                cur_st = (i, j)
                dq = deque([cur_st])
                vis_map[i][j] = True
                
                while dq:
                    cur_point = dq.pop()
                    # 4방탐색
                    for d in range(4):
                        nx = cur_point[0] + dx[d]
                        ny = cur_point[1] + dy[d]
                        # 정상범위 이면서 배추 이면서 미방문일때
                        if 0<=nx<N and 0<=ny<M and input_map[nx][ny] == 1 and vis_map[nx][ny] == False:
                            dq.appendleft((nx, ny))
                            vis_map[nx][ny] = True
    print(res)