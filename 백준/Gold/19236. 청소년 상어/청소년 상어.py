"""
물고기의 정보는 두 정수 ai, bi로 이루어져 있고, ai는 물고기의 번호, bi는 방향
방향 bi는 8보다 작거나 같은 자연수를 의미하고, 1부터 순서대로 ↑, ↖, ←, ↙, ↓, ↘, →, ↗ 를 의미한다.
7 6 2 3 15 6 9 8
3 1 1 8 14 7 10 1
6 1 13 6 4 3 11 4
16 1 8 7 5 2 12 2
"""
import copy

input_map = [[], [], [], []]

# . ↑, ↖, ←, ↙, ↓, ↘, →, ↗ (1 부터)
dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]

max_point = -1


class Fish:
    def __init__(self, f_id, f_dir):
        self.id = f_id
        self.dir = f_dir

    def __str__(self):
        return f'fish_id: {self.id}, fish_dir: {self.dir}'


class Shark:
    def __init__(self, s_dir, s_point, s_pos):
        self.dir = s_dir
        self.point = s_point
        self.pos = s_pos

    def __str__(self):
        return f's_dir: {self.dir}, s_point: {self.point}, s_pos : {self.pos}'


from collections import defaultdict

fish_pos_dict = defaultdict(tuple)

for i in range(4):
    row_infos = input().split(" ")
    col_cnt = 0
    for j in range(0, 7, 2):
        fish_id = int(row_infos[j])
        fish_dir = int(row_infos[j+1])
        input_map[i].append(Fish(fish_id, fish_dir))
        fish_pos_dict[fish_id] = (i, col_cnt)  # 물고기 위치 저장 딕셔너리
        col_cnt += 1


def get_shark_dst_list(shk_obj, cur_map):
    dst_lst = []
    shk_dst = shk_obj.dir
    shk_pos = shk_obj.pos
    sx = shk_pos[0]
    sy = shk_pos[1]
    _dx = dx[shk_dst]
    _dy = dy[shk_dst]
    # 상어 방향에따라 현재 상어의 위치와 더해주기 (정상 범위이면서 물고기가 있을때만 가능)
    while True:
        sx += _dx
        sy += _dy
        # 정상범위 밖이면 루프 끝
        if not (0 <= sx < 4 and 0 <= sy < 4):
            break

        if cur_map[sx][sy] is not None:
            dst_lst.append((sx, sy))

    return dst_lst


def move_fish(c_map, cur_fpd):
    # 물고기는 번호가 작은 물고기부터 순서대로 이동한다. o
    # 물고기는 한 칸을 이동할 수 있고, 이동할 수 있는 칸은 빈 칸과 다른 물고기가 있는 칸, o
    # 이동할 수 없는 칸은 상어가 있거나, 공간의 경계를 넘는 칸이다. o
    # 각 물고기는 방향이 이동할 수 있는 칸을 향할 때까지 방향을 45도 반시계 회전시킨다. o
    # 만약, 이동할 수 있는 칸이 없으면 이동을 하지 않는다. 그 외의 경우에는 그 칸으로 이동을 한다. o
    # 물고기가 다른 물고기가 있는 칸으로 이동할 때는 서로의 위치를 바꾸는 방식으로 이동한다. o

    for cur_fish_id in range(1, 17):
        cur_fish_pos = cur_fpd[cur_fish_id]
        if not cur_fish_pos:
            continue
        fx = cur_fish_pos[0]
        fy = cur_fish_pos[1]
        cur_fish = c_map[fx][fy]
        cur_fish_dir = cur_fish.dir
        for d in range(cur_fish_dir, cur_fish_dir+8):
            if d > 8:
                d = d % 8
            _dx = dx[d]
            _dy = dy[d]
            nx = fx + _dx
            ny = fy + _dy
            # next에 상어가 없거나 정상범위 일때만 이동 진행
            if (0 <= nx < 4 and 0 <= ny < 4) and not isinstance(c_map[nx][ny], Shark):
                # fish의 방향 바꾸기
                cur_fish.dir = d
                # 서로의 위치를 바꾸기 (지도상, 딕셔너리상 둘 다 바꾸기)
                nxt_fish = c_map[nx][ny]
                # 지도상
                c_map[fx][fy] = nxt_fish
                c_map[nx][ny] = cur_fish
                # 딕셔너리상
                if nxt_fish is None:
                    # 현 fish 자리 값 바꾸기
                    cur_fpd[cur_fish_id] = (nx, ny)
                else:
                    nxt_fish_id = nxt_fish.id
                    cur_fpd[nxt_fish_id] = (fx, fy)
                    cur_fpd[cur_fish_id] = (nx, ny)
                break


def dfs(cur_map, dst_pos, f_p_dict, cur_shark):
    global max_point

    c_map = copy.deepcopy(cur_map)
    cur_fpd = f_p_dict.copy()

    if cur_shark is None:
        # 상어 초기 세팅
        init_fish = c_map[0][0]
        shk = Shark(init_fish.dir, init_fish.id, (0, 0))
        c_map[0][0] = shk
        # 물고기 사망 처리
        cur_fpd.pop(init_fish.id)
        # 물고기 이동 진행
        move_fish(c_map, cur_fpd)
        # 상어가 갈 수 있는 곳으로 진행
        shark_dst_list = get_shark_dst_list(shk, c_map)
        if not shark_dst_list:
            # 상어가 갈 수 있는 곳이 없으므로 현재 상어의 point를 글로벌 변수와 비교 및 저장하고 return
            cur_shk_point = shk.point
            if cur_shk_point > max_point:
                max_point = cur_shk_point
                return
        for dst_tup in shark_dst_list:
            dfs(c_map, dst_tup, cur_fpd, shk)
    else:
        # 상어 이동
        dst_x = dst_pos[0]
        dst_y = dst_pos[1]
        dst_fish = cur_map[dst_x][dst_y]
        shk = Shark(dst_fish.dir, (cur_shark.point + dst_fish.id), (dst_x, dst_y))
        c_map[cur_shark.pos[0]][cur_shark.pos[1]] = None
        c_map[dst_x][dst_y] = shk
        # 물고기 사망 처리
        cur_fpd.pop(dst_fish.id)
        # 물고기 이동 진행
        move_fish(c_map, cur_fpd)
        # 상어가 갈 수 있는 곳으로 진행
        shark_dst_list = get_shark_dst_list(shk, c_map)
        if not shark_dst_list:
            # 상어가 갈 수 있는 곳이 없으므로 현재 상어의 point를 글로벌 변수와 비교 및 저장하고 return
            cur_shk_point = shk.point
            if cur_shk_point > max_point:
                max_point = cur_shk_point
                return
        # 다음 dfs
        for dst_tup in shark_dst_list:
            dfs(c_map, dst_tup, cur_fpd, shk)


dfs(input_map, (0, 0), fish_pos_dict, None)

print(max_point)