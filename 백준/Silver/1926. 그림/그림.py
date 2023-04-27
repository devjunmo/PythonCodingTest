"""6 5
1 1 0 1 1
0 1 1 0 0
0 0 0 0 0
1 0 1 1 1
0 0 1 1 1
0 0 1 1 1
"""

from collections import deque

NM = list(map(int, input().split(" ")))

# 상우하좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N = NM[0]
M = NM[1]

obj_cnt = 0
max_cnt = 0

input_arr = []

vis_arr = []
for _ in range(N):
    vis_arr.append([False]*M)

for _ in range(N):
    input_arr.append(list(map(int, input().split(" "))))

def bfs(st_tup):
    global obj_cnt
    
    obj_cnt += 1 # 도형의 갯수 증가
    cnt = 1  # 첫발 밟아서 1부터 시작
    vis_arr[st_tup[0]][st_tup[1]] = True
    dq = deque([st_tup])
    
    while len(dq) != 0:
        cur_point = dq.pop()
        
        for i in range(4):
            nxt_x = cur_point[0] + dx[i]
            nxt_y = cur_point[1] + dy[i]
            
            # 정상범위 and 방문x
            if 0 <= nxt_x < N and 0 <= nxt_y < M and vis_arr[nxt_x][nxt_y] == False and input_arr[nxt_x][nxt_y] == 1:
                # 큐에 담고 방문 체크하기
                dq.appendleft((nxt_x, nxt_y))
                vis_arr[nxt_x][nxt_y] = True
                # cnt ++
                cnt += 1

    return cnt


for i in range(N):
    for j in range(M):
        if input_arr[i][j] == 1 and vis_arr[i][j] == False:
            cur_cnt = bfs((i,j))
            if max_cnt < cur_cnt:
                max_cnt = cur_cnt

print(obj_cnt)
print(max_cnt)