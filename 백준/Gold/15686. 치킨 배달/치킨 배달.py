"""
5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2
"""

N, M = list(map(int, input().split(" ")))
input_map = [list(map(int, input().split(" "))) for _ in range(N)]

from pprint import pprint
# pprint(input_map)

house_lst = []
chicks_lst = []

# 모든 포인트를 다 돌며 1, 2의 좌표를 따기
for i in range(N):
    for j in range(N):
        if input_map[i][j] == 1:  # 일반 집일 때
            house_lst.append((i, j))
        elif input_map[i][j] == 2:  # 치킨집 일 때
            chicks_lst.append((i, j))


# 치킨집 조합 경우의 수 구하기
ch_len = len(chicks_lst)

min_city_chick_dist = 9999999999
chick_comb_case = [() for _ in range(M)]


def comb(lev, st):
    global min_city_chick_dist

    if lev == M:
        tmp_chick_dist_lst = []
        # 현재 나온 치킨집 조합 경우의 수에 대해 가정집과 비교하여 도시의 치킨거리를 구하고 그걸 min값과 비교
        # 가정집을 모두 루프돌면서 집 하나당 치킨집들과 거리 비교하여 가장 작은애를 저장
        # 저장한 임시리스트를 모두 더하면 도시의 치킨거리가 나옴. 그거를 전역 도치킨거리와 비교하여 min값 가져가기

        # 거리비교 로직 ...
        for house in house_lst:
            tmp_min_dist = 9999999999
            h_x = house[0]
            h_y = house[1]
            for chick_pos in chick_comb_case:
                c_x = chick_pos[0]
                c_y = chick_pos[1]
                # 임의의 두 칸 (r1, c1)과 (r2, c2) 사이의 거리는 |r1-r2| + |c1-c2|로 구한다.
                cur_dist = abs(h_x-c_x) + abs(h_y-c_y)
                if cur_dist < tmp_min_dist:
                    tmp_min_dist = cur_dist
            # 가장 치킨 거리가 작은 집을 저장
            tmp_chick_dist_lst.append(tmp_min_dist)

        city_chick_dist = sum(tmp_chick_dist_lst)
        if city_chick_dist < min_city_chick_dist:
            min_city_chick_dist = city_chick_dist

        return

    for i in range(st, ch_len):
        chick_comb_case[lev] = chicks_lst[i]
        comb(lev+1, i+1)


comb(0, 0)

print(min_city_chick_dist)














