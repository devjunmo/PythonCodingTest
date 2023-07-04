from pprint import pprint

N = int(input())

# NxN 배열 생성
map_lst = [[0] * N for _ in range(N)]

# dp 배열 생성
dp = [[0] * N for _ in range(N)]

for i in range(N):
    tmp_row = list(map(int, input().split(" ")))
    for j in range(len(tmp_row)):
        map_lst[i][j] = tmp_row[j]

# pprint(map_lst)
dp[0][0] = map_lst[0][0]

if N == 1:
    print(dp[0][0])
else:
    for i in range(1, N):
        for j in range(i+1):
            lu = -1
            u = -1
            # 좌상이 정상범위 일 때
            lu_x = i - 1
            lu_y = j - 1
            if 0 <= lu_x < N and 0 <= lu_y < N:
                lu = dp[lu_x][lu_y]
            
            # 상이 정상범위일 때
            u_x = i - 1
            u_y = j
            if 0 <= u_x < N and 0 <= u_y < N:
                u = dp[u_x][u_y]
            
            dp[i][j] = map_lst[i][j] + max(lu, u)


    res = -1

    # 가장 큰 수 찾기
    for i in range(N):
        for j in range(N):
            if dp[i][j] > res:
                res = dp[i][j]

    print(res)