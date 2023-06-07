import sys
from collections import deque, defaultdict

# 입력은 sys.stdin.readline() 대신 input() 사용, 예제에 맞추어 사용합니다.
N = int(input())
input_map = [list(map(int, input().split(" "))) for _ in range(N)]

shark_pos = ()
shark_size = 2
for i in range(N):
    for j in range(N):
        if input_map[i][j] == 9:
            shark_pos = (i, j)

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

# 딕셔너리 선언을 함수 외부로 이동
dist_dict = defaultdict(lambda: -1)

def bfs(sp, fp):
    dist_dict.clear()  # 매 호출시 딕셔너리 초기화
    target_x = fp[0]
    target_y = fp[1]

    dq = deque([sp])  
    dist_dict[sp] = 0

    while dq:
        cur_pos = dq.pop()
        cx = cur_pos[0]
        cy = cur_pos[1]
        for cd in range(4):
            nx = cx + dx[cd]
            ny = cy + dy[cd]
            if 0 <= nx < N and 0 <= ny < N and dist_dict[(nx, ny)] == -1 and input_map[nx][ny] <= shark_size:
                if nx == target_x and ny == target_y:
                    cur_dist_val = dist_dict[(cx, cy)]
                    return cur_dist_val + 1
                dq.appendleft((nx, ny))
                dist_dict[(nx, ny)] = dist_dict[(cx, cy)] + 1
    return -1

def get_able_to_eat_fish(ss):
    food_tup_lst = []
    for _i in range(N):
        for _j in range(N):
            if input_map[_i][_j] != 0 and input_map[_i][_j] < ss:
                food_tup_lst.append((_i, _j))
    return food_tup_lst

res = 0
exp = 0

while True:
    food_pos_list = get_able_to_eat_fish(shark_size)
    min_dist_food = 99999999
    min_dist_fp = ()

    for fp in food_pos_list:
        fp_dist = bfs(shark_pos, fp)
        if fp_dist != -1 and min_dist_food > fp_dist:
            min_dist_food = fp_dist
            min_dist_fp = fp

    if min_dist_fp == ():
        break

    res += min_dist_food

    spx = shark_pos[0]
    spy = shark_pos[1]
    fpx = min_dist_fp[0]
    fpy = min_dist_fp[1]

    input_map[spx][spy] = 0
    input_map[fpx][fpy] = 9
    shark_pos = min_dist_fp

    exp += 1
    if exp == shark_size:
        shark_size += 1
        exp = 0

print(res)
