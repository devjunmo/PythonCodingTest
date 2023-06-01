"""
4
4 3 2 1
0 0 0 0
0 0 9 0
1 2 3 4
"""
import sys

input = sys.stdin.readline
N = int(input())
input_map = [list(map(int, input().split(" "))) for _ in range(N)]
from pprint import pprint

# pprint(input_map)

# 아기상어 위치 찾기
shark_pos = ()
shark_size = 2
for i in range(N):
    for j in range(N):
        if input_map[i][j] == 9:
            shark_pos = (i, j)


from collections import deque, defaultdict


# 상좌우하
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


def bfs(sp, fp):
    blocking = True  # 타겟에 도달할 수 있는지 없는지 체크 하는 용도
    target_x = fp[0]
    target_y = fp[1]
    dist_dict = defaultdict(lambda: -1)  # dist 기록용

    dq = deque([sp])  # 시작 점은 현재 상어 위치
    dist_dict[sp] = 0  # 시작점은 거리가 영

    while dq:
        cur_pos = dq.pop()  # 현재 상어 위치
        cx = cur_pos[0]
        cy = cur_pos[1]
        for cd in range(4):
            nx = cx + dx[cd]
            ny = cy + dy[cd]
            # 정상범위이면서 방문 안했으면서 상어보다 작거나 같을 때
            if 0 <= nx < N and 0 <= ny < N and dist_dict[(nx, ny)] == -1 and input_map[nx][ny] <= shark_size:
                # 만약 nx, ny가 타겟이랑 똑같다면 끝내기
                if nx == target_x and ny == target_y:
                    cur_dist_val = dist_dict[(cx, cy)]
                    return cur_dist_val + 1
                dq.appendleft((nx, ny))
                dist_dict[(nx, ny)] = dist_dict[(cx, cy)] + 1
    if blocking:
        return -1


def get_able_to_eat_fish(ss):
    food_tup_lst = []  # 튜플 리스트
    for _i in range(N):
        for _j in range(N):
            if input_map[_i][_j] != 0 and input_map[_i][_j] < ss:
                food_tup_lst.append((_i, _j))
    return food_tup_lst


res = 0
exp = 0

while True:
    # 1. 나보다 작은 물고기들 위치 가져오기
    food_pos_list = get_able_to_eat_fish(shark_size)
    # 2. 해당 푸드 위치에 대해 bfs 돌며 최단거리인 푸드를 선택하기
    min_dist_food = 99999999
    min_dist_fp = ()
    for fp in food_pos_list:
        fp_dist = bfs(shark_pos, fp)
        # 도달할 수 있으 면서 최소인 거리일 때 (-1이면 도달할 수 없는 거리임)
        if fp_dist != -1 and min_dist_food > fp_dist:
            min_dist_food = fp_dist
            min_dist_fp = fp

    # 만약 먹잇감들 루프를 다 돌았는데도 현재 위치에서 갈 수 있는게 없다면 엄마 콜
    if min_dist_fp == ():
        break

    # 상어 이동 카운트 갱신
    res += min_dist_food

    # 상어 위치와 경험치, 크기 변동
    spx = shark_pos[0]
    spy = shark_pos[1]
    fpx = min_dist_fp[0]
    fpy = min_dist_fp[1]

    # 상어 위치 변동
    input_map[spx][spy] = 0
    input_map[fpx][fpy] = 9
    shark_pos = min_dist_fp

    # 상어 경험치 증가
    exp += 1
    if exp == shark_size:
        shark_size += 1
        exp = 0


print(res)












