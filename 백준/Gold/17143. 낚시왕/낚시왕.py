"""
4 6 8
4 1 3 3 8
1 3 5 2 9
2 4 8 4 1
4 5 0 1 4
3 3 1 2 7
1 5 8 4 3
3 6 2 1 2
2 2 2 3 5
"""

import time, sys
R, C, M = list(map(int, input().split(" ")))
res = 0


class Shark:
    def __init__(self, _r, _c, _s, _d, _z, _id):
        self.pos = (_r, _c)
        self.speed = _s
        self.dir = _d
        self.size = _z
        self.id = _id

    def __str__(self):
        return f'id: {self.id}, pos: {self.pos}, speed: {self.speed}, dir: {self.dir}, size: {self.size}'


# shark_list = []  # 상어 객체들 관리
from collections import defaultdict

shark_dict = defaultdict(Shark)  # key = id, value = 상어객체

input_map = [[None] * (C+1) for _ in range(R+1)]  # 1부터 시작, 0위치는 무시

dir_dict = {1: (-1, 0), 2: (1, 0), 3: (0, 1), 4: (0, -1)}  # 상하우좌

for s_id in range(M):
    r, c, s, d, z = list(map(int, input().split(" ")))

    # 상어 딕셔너리에 데이터 적재
    shark_obj = Shark(r, c, s, d, z, s_id)

    shark_dict[s_id] = shark_obj

    # input_map에 상어 위치 놓기
    input_map[r][c] = shark_obj


def remove_shark(_shk_obj):
    # 상어 자리 None 으로 바꾸기
    sx = _shk_obj.pos[0]
    sy = _shk_obj.pos[1]
    input_map[sx][sy] = None

    # 상어 딕셔너리에서 해당 상어 제거
    shark_dict.pop(_shk_obj.id)


def get_fish(_cur_sec):
    global res

    # 현재 컬럼에 존재 하는 상어 중 row가 가장 작은 상어 선택 후
    cur_shark_lst = []
    for i in range(1, R+1):
        cur_shark = input_map[i][_cur_sec]
        if cur_shark is not None:
            cur_shark_lst.append(cur_shark)
    if cur_shark_lst:
        get_my_fish = cur_shark_lst[0]
        # res += 상어 사이즈 후
        res += get_my_fish.size
        # 상어 제거
        remove_shark(get_my_fish)


def process_set_pos(_cur_pos, _dir, _speed):
    cur_dir = _dir  # 현 시점 방향
    cur_pos = _cur_pos

    move_size = 0
    if cur_dir == 1 or cur_dir == 2:
        # 상, 하 일때는
        move_size = R
    else:
        # 우, 좌 일때는
        move_size = C

    back_to_cur_pos = (move_size * 2) - 2
    calc_speed = _speed % back_to_cur_pos

    for i in range(calc_speed):
        go = dir_dict.get(cur_dir)

        cx = cur_pos[0]
        cy = cur_pos[1]

        nx = cx + go[0]
        ny = cy + go[1]

        if 1 <= nx <= R and 1 <= ny <= C:
            # 정상 범위면 다음 으로 진행
            cur_pos = (nx, ny)
        else:
            # 정상 범위가 아니면 방향 반대로 바꾸고 다시 진행
            # 상->하 / 하->상 / 우->좌 / 좌->우
            if cur_dir == 1:
                cur_dir = 2
            elif cur_dir == 2:
                cur_dir = 1
            elif cur_dir == 3:
                cur_dir = 4
            elif cur_dir == 4:
                cur_dir = 3

            go = dir_dict.get(cur_dir)

            nx = cx + go[0]
            ny = cy + go[1]

            cur_pos = (nx, ny)

    return (cur_pos, cur_dir)


def set_new_pos(_cur_srk):
    # 1. 상, 2. 하, 3. 우, 4. 좌
    cur_dir = _cur_srk.dir
    shark_speed = _cur_srk.speed
    result_pos, result_dir = process_set_pos(_cur_srk.pos, cur_dir, shark_speed)
    # 상어 위치 갱신
    _cur_srk.pos = result_pos
    _cur_srk.dir = result_dir


def del_dup_pos(_shark_lst):
    dup_list_dict = defaultdict(list)
    for shk in _shark_lst:
        cur_pos = shk.pos
        dup_list_dict[cur_pos].append(shk)

    # 중복 있는 리스트에서 가장 size가 큰것만 남기기
    for k, v in dup_list_dict.items():
        if len(v) >= 2:
            max_size = -1
            max_size_id = -1
            for shk in v:
                if shk.size > max_size:
                    max_size = shk.size
                    max_size_id = shk.id
            for shk in v:
                if shk.id != max_size_id:
                    rmv_id = shk.id
                    shark_dict.pop(rmv_id)
                    # input map에 해당 상어 제거
                    # rm_x = shk.pos[0]
                    # rm_y = shk.pos[1]
                    # input_map[rm_x][rm_y] = None


def set_shark_to_input_map(_shark_lst):
    global input_map
    # input_map에 있는 기존의 shark id의 상어는 제거하고
    input_map = [[None] * (C + 1) for _ in range(R + 1)]

    # 새로운 상어 딕셔너리의 상어를 맵에 넣기
    shark_lst = list(shark_dict.values())
    for shk in shark_lst:
        shk_pos = shk.pos
        sx = shk_pos[0]
        sy = shk_pos[1]
        input_map[sx][sy] = shk
        # if input_map[sx][sy] is None:
        #     input_map[sx][sy] = shk
        # else:
        #     prev_shk_obj = input_map[sx][sy]
        #     if prev_shk_obj.size < shk.size:
        #         input_map[sx][sy] = shk


# def del_dup_pos2(shark_lst):
#     pass


def move_shark():
    # 상어 딕셔너리의 value를 다 가져옴
    shark_lst = list(shark_dict.values())
    for srk in shark_lst:
        set_new_pos(srk)

    # 상어 중복 처리
    del_dup_pos(shark_lst)
    shark_lst = list(shark_dict.values())
    set_shark_to_input_map(shark_lst)


for cur_sec in range(1, C+1):
    # 낚시 하기
    get_fish(cur_sec)
    # print(f'낚시 소요 시간: {round(time.time() - whole_st_time)} ')
    # 상어 이동하기
    move_shark()
    # print(f'상어 이동 소요 시간: {round(time.time() - whole_st_time)} ')


print(res)
