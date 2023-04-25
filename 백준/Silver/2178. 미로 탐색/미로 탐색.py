"""
4 6
101111
101010
101011
111011
"""

# 사방탐색 -> 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

NM = list(map(int, input().split(" ")))

N = NM[0]
M = NM[1]

st_point = (0, 0)
end_point = (N-1, M-1)

input_lst = []

dist_lst = []
for _ in range(N):
    dist_lst.append([-1] * M) 

for i in range(N):
    tmp_lst = [int(x) for x in input()]
    input_lst.append(tmp_lst)

# print(input_lst)

from collections import deque

q = deque([])

# appendleft, pop조합

# 첫 위치 방문 체크
q.appendleft(st_point)
dist_lst[st_point[0]][st_point[1]] = 0  # 첫 위치는 거리가 영


while len(q) > 0:
    cur_point = q.pop()
    # 사방탐색
    for i in range(4):
        nxt_x = cur_point[0] + dx[i]
        nxt_y = cur_point[1] + dy[i]
        # 정상범위이면서 갈수있는곳이면서 방문 안했을때
        if 0<=nxt_x<N and 0<=nxt_y<M and dist_lst[nxt_x][nxt_y] == -1 and input_lst[nxt_x][nxt_y] == 1:
            q.appendleft((nxt_x, nxt_y)) # 큐에 넣고
            dist_lst[nxt_x][nxt_y] = dist_lst[cur_point[0]][cur_point[1]] + 1

print(dist_lst[N-1][M-1] + 1)