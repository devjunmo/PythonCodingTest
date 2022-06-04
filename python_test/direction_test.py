
# 8 방향
# 북0 북동1 동2 동남3
# 남4 남서5 서6 서북7
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

d_arr = [[0] * 3 for _ in range(3)]

cur_x = 1
cur_y = 1

print('start')
d_arr[cur_x][cur_y] = 1
[print(arr) for arr in d_arr]

print('북동')
direct = 1

d_arr[cur_x + dx[direct]][cur_y + dy[direct]] = 1
[print(arr) for arr in d_arr]
