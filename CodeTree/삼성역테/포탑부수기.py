
from collections import deque


class Tower:
    def __init__(self, _damage, _turn, _x, _y):
        self.damage = _damage
        self.turn = _turn
        self.sum_xy = _x + _y
        self.x = _x
        self.y = _y

    def __str__(self):
        return f"damage: {self.damage}, turn: {self.turn}, sumXY: {self.sum_xy}, x: {self.x}, y: {self.y}"


N, M, K = list(map(int, input().split(" ")))
input_map = [[Tower(-1, -1, -1, -1)] * M for _ in range(N)]

# 레이저: 우/하/좌/상
l_dx = [0, 1, 0, -1]
l_dy = [1, 0, -1, 0]
vis_lst = [[False] * M for _ in range(N)]

# 포탄 : 8방향: 우/ 우하/ 하/ 하좌/ 좌/ 좌상/ 상/ 상우
p_dx = [0, 1, 1, 1, 0, -1, -1, -1]
p_dy = [1, 1, 0, -1, -1, -1, 0, 1]

for i in range(N):
    tmp_row = list(map(int, input().split(" ")))
    for j in range(M):
        t_dam = tmp_row[j]
        input_map[i][j] = Tower(t_dam, 0, i, j)  # 대미지, 턴, 위치 정보 세팅

curTurn = 1


def select_attacker():
    # 공격력이 가장 낮은 포탑이 가장 약한 포탑입니다.
    # 만약 공격력이 가장 낮은 포탑이 2개 이상이라면, 가장 최근에 공격한 포탑이 가장 약한 포탑입니다. (모든 포탑은 시점 0에 모두 공격한 경험이 있다고 가정하겠습니다.)
    # 만약 그러한 포탑이 2개 이상이라면, 각 포탑 위치의 행과 열의 합이 가장 큰 포탑이 가장 약한 포탑입니다.
    # 만약 그러한 포탑이 2개 이상이라면, 각 포탑 위치의 열 값이 가장 큰 포탑이 가장 약한 포탑입니다.
    tower_lst = []
    for _i in range(N):
        for _j in range(M):
            if not is_destroy_tower(_i, _j):
                tower_lst.append(input_map[_i][_j])

    tower_lst.sort(key=lambda tower: (tower.damage, -tower.turn, -tower.sum_xy, -tower.y))
    atker_pos = (tower_lst[0].x, tower_lst[0].y)
    # 공격자의 대미지 갱신 및 턴 갱신
    atk_tower = tower_lst[0]
    atk_tower.damage += (N + M)
    atk_tower.turn = curTurn
    # 공격자 위치 리턴
    return atker_pos


def select_target(ap):
    # 공격자를 제외하고!!! 공격력이 가장 높은 포탑이 가장 강한 포탑입니다.
    # 만약 공격력이 가장 높은 포탑이 2개 이상이라면, 공격한지 가장 오래된 포탑이 가장 강한 포탑입니다. (모든 포탑은 시점 0에 모두 공격한 경험이 있다고 가정하겠습니다.)
    # 만약 그러한 포탑이 2개 이상이라면, 각 포탑 위치의 행과 열의 합이 가장 작은 포탑이 가장 강한 포탑입니다.
    # 만약 그러한 포탑이 2개 이상이라면, 각 포탑 위치의 열 값이 가장 작은 포탑이 가장 강한 포탑입니다.
    tower_lst = []
    for _i in range(N):
        for _j in range(M):
            if not is_destroy_tower(_i, _j) and (_i, _j) != ap:
                tower_lst.append(input_map[_i][_j])
    tower_lst.sort(key=lambda tower: (-tower.damage, tower.turn, tower.sum_xy, tower.y))
    atker_pos = (tower_lst[0].x, tower_lst[0].y)
    return atker_pos


# 부서진 타워 인지 체크하는 메소드
def is_destroy_tower(x_pos, y_pos):
    # input_map에서 해당 위치인 tower 객체의 damage 필드가 영이면 부서진 타워
    if input_map[x_pos][y_pos].damage == 0:
        return True  # 부숴짐
    return False  # 안 부숴짐


def mirror(_point_num, _NM):
    return _point_num % _NM


def edge_mirror():
    pass


def apply_raser_damage(dam_path_lst):
    lst_size = len(dam_path_lst)  # 좌표 튜플 리스트
    atker_damage = -1
    for _i in range(lst_size):
        if _i == 0:  # 공격자 일때
            atk_pos = dam_path_lst[_i]
            apx, apy = atk_pos[0], atk_pos[1]
            atker_damage = input_map[apx][apy].damage
        elif _i == lst_size-1:  # 타겟 일 때
            tgt_pos = dam_path_lst[_i]
            tx, ty = tgt_pos[0], tgt_pos[1]
            tgt_dmg = input_map[tx][ty].damage
            input_map[tx][ty].damage = max(0, tgt_dmg-atker_damage)
        else:  # 나머지 일 때
            etc_pos = dam_path_lst[_i]
            ex, ey = etc_pos[0], etc_pos[1]
            etc_dmg = input_map[ex][ey].damage
            input_map[ex][ey].damage = max(0, etc_dmg - atker_damage//2)


def raser_attack(ap, tp):
    # 상하좌우의 4개의 방향으로 움직일 수 있습니다.
    # 부서진 포탑이 있는 위치는 지날 수 없습니다.
    # 가장자리에서 막힌 방향으로 진행하고자 한다면, 반대편으로 나옵니다.
    # (예를 들어, 위의 예시에서 (2,3)에서 오른쪽으로 두번 이동한다면, (2,3) -> (2,4) -> (2,1) 순으로 이동합니다.)
    # 우/하/좌/상의 우선순위대로 먼저 움직인 경로가 선택됩니다.
    # 공격 대상에는 공격자의 공격력 만큼의 피해를 입히며, 피해를 입은 포탑은 해당 수치만큼 공격력이 줄어듭니다.
    # 또한 공격 대상을 제외한 레이저 경로에 있는 포탑도 공격을 받게 되는데, 이 포탑은 공격자 공격력의 절반 만큼의 공격을 받습니다.
    # (절반이라 함은 공격력을 2로 나눈 몫을 의미합니다.)

    ax, ay = ap[0], ap[1]
    dq = deque([(ax, ay, [ap])])  # x, y, [경로(위치 튜플)]
    vis_lst[ax][ay] = True  # 공격자 방문 체크

    while dq:
        cur_pos_info = dq.pop()
        cx = cur_pos_info[0]
        cy = cur_pos_info[1]
        # cur_path_lst = cur_pos_info[2].copy()

        for d in range(4):
            cur_path_lst = cur_pos_info[2].copy()
            nx = mirror(cx + l_dx[d], N)
            ny = mirror(cy + l_dy[d], M)
            if not vis_lst[nx][ny] and not is_destroy_tower(nx, ny):
                # 미 방문이면서 부서지지 않은 타워일때만
                nxt_pos = (nx, ny)
                cur_path_lst.append(nxt_pos)
                dq.appendleft((nx, ny, cur_path_lst))
                vis_lst[nx][ny] = True  # 방문 체크
                # 만약 타겟에 도달 했다면
                if nxt_pos == tp:
                    apply_raser_damage(cur_path_lst)  # 레이저 대미지 적용
                    return cur_path_lst  # 경로 리턴


def potan_attack(ap, tp):
    battle_lst = [ap, tp]
    # 공격 대상은 공격자 공격력 만큼의 피해를 받습니다.  o
    # 추가적으로 주위 8개의 방향에 있는 포탑도 피해를 입는데, 공격자 공격력의 절반 만큼의 피해를 받습니다.
    # (절반이라 함은 공격력을 2로 나눈 몫을 의미합니다.) 공격자는 해당 공격에 영향을 받지 않습니다.
    # 만약 가장자리에 포탄이 떨어졌다면, 위에서의 레이저 이동처럼 포탄의 추가 피해가 반대편 격자에 미치게 됩니다.
    ax = ap[0]
    ay = ap[1]
    atk_tower = input_map[ax][ay]
    atk_tower_damage = atk_tower.damage
    # 공격자 턴 갱신
    atk_tower.turn = curTurn

    tx = tp[0]
    ty = tp[1]
    tgt_tower = input_map[tx][ty]
    # 공격 대상은 공격자 공격력 만큼의 피해를 받습니다.
    tgt_tower.damage = max(0, (tgt_tower.damage - atk_tower_damage))
    # 타겟 포지션으로 부터 8방향 체크
    for d in range(8):
        # nx, ny = tx + p_dx[d], ty + p_dy[d]
        nx = mirror(tx + p_dx[d], N)
        ny = mirror(ty + p_dy[d], M)
        next_tup = (nx, ny)
        # 부서진 포탑이 아니라면 -> 배틀리스트 등록, 대미지 절반 피해 적용, 그리고 배틀 리스트에 없을때!
        if not is_destroy_tower(nx, ny) and next_tup not in battle_lst:
            battle_lst.append(next_tup)
            input_map[nx][ny].damage = max(0, input_map[nx][ny].damage - atk_tower_damage//2)

    return battle_lst


def repair_tower(atk_path_lst):
    # 공격과 무관했던 다음 4개의 포탑은 정비를 받아 공격력이 1씩 증가
    for _i in range(N):
        for _j in range(M):
            if (_i, _j) not in atk_path_lst and not is_destroy_tower(_i, _j):
                input_map[_i][_j].damage += 1


def get_alive_tower_count():
    cnt = 0
    for _i in range(N):
        for _j in range(M):
            if input_map[_i][_j].damage != 0:
                cnt += 1
    return cnt


def reset_visit_lst():
    # 방문 배열 초기화
    for _i in range(N):
        for _j in range(M):
            vis_lst[_i][_j] = False


while curTurn <= K:
    # 1. 공격자 선정
    attacker_pos = select_attacker()

    # 2. 타겟 선정
    target_pos = select_target(attacker_pos)

    # 3. 레이저 공격
    attack_path = raser_attack(attacker_pos, target_pos)
    reset_visit_lst()

    if attack_path is None:
        attack_path = []

    if not attack_path:
        # 레이저 공격 실패시 포탄 공격
        attack_path += potan_attack(attacker_pos, target_pos)

    # 4. 포탑 부서짐 -> 구현 의미 없음
    # 5. 포탑 정비
    repair_tower(attack_path)

    # 현재 턴 증가
    curTurn += 1

    # 생존 타워가 1개라면
    if get_alive_tower_count() == 1:
        break


max_damage = -1
for i in range(N):
    for j in range(M):
        if input_map[i][j].damage != 0:
            max_damage = max(input_map[i][j].damage, max_damage)

print(max_damage)
