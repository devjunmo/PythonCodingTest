N = int(input())

stair_lst = []

for _ in range(N):
    stair_lst.append(int(input()))

if N == 1:
    print(stair_lst[0])
elif N == 2:
    print(stair_lst[0] + stair_lst[1])
else:
    dp = []
    for _ in range(N):
        dp.append([0]*3)


    dp[0][1] = stair_lst[0] # 여기 포함 연속 1개
    dp[0][2] = stair_lst[0] # 여기 포함 연속 2개
    
    dp[1][1] = stair_lst[1]
    dp[1][2] = stair_lst[1] + dp[0][1]

    for i in range(2, N):
        
        dp[i][1] = stair_lst[i] + max(dp[i-2][1], dp[i-2][2])
        dp[i][2] = stair_lst[i] + dp[i-1][1]
    print(max(dp[N-1][1], dp[N-1][2]))