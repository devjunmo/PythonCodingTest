TC = int(input())

for c_num in range(1, TC+1):
    N = int(input())
    map_arr = [list(map(int, list(input()))) for _ in range(N)]
    # print(map_arr)

    half_len = int(N/2)
    res = 0

    for i in range(N):
        if i <= half_len:
            start = half_len - i
            end = half_len + i
            for j in range(start, end+1):
                res += map_arr[i][j]
        else:
            start = half_len - (N - i - 1)
            end = half_len + (N - i - 1)
            for j in range(start, end+1):
                res += map_arr[i][j]

    print(f'#{c_num} {res}')
