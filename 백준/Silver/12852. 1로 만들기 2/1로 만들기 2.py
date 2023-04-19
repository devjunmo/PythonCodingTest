
N = int(input())

"""
X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.
"""
dp = []

# 초항 대입
dp.append(0)  # dp[0] = 0
dp.append(0)  # dp[1] = 0
dp.append(1)  # dp[2] = 1
dp.append(1)  # dp[3] = 1

# dp[i] 채우기
for i in range(4, N+1):
    tmp_lst = []
    if i % 3 == 0:
        tmp_lst.append(dp[int(i/3)])
    if i % 2 == 0:
        tmp_lst.append(dp[int(i/2)])
    tmp_lst.append(dp[i-1])
    min_val = min(tmp_lst)
    # dp[i] = min_val + 1
    dp.append(min_val + 1)

# dp 테이블 탐색 하며 경로 찾기
cur_val = N
ans_arr = [N]

while cur_val != 1:
    tmp_lst = [99999999] * 3
    tmp_val_lst = [-1] * 3
    if cur_val % 3 == 0:
        tmp_lst[0] = dp[int(cur_val / 3)]
        tmp_val_lst[0] = (int(cur_val / 3))
    if cur_val % 2 == 0:
        tmp_lst[1] = dp[int(cur_val / 2)]
        tmp_val_lst[1] = (int(cur_val / 2))
    tmp_lst[2] = dp[cur_val - 1]
    tmp_val_lst[2] = (cur_val - 1)
    min_val = min(tmp_lst)
    min_idx = tmp_lst.index(min_val)

    ans_arr.append(tmp_val_lst[min_idx])
    cur_val = tmp_val_lst[min_idx]


print(dp[N])
print(" ".join(map(str, ans_arr)))