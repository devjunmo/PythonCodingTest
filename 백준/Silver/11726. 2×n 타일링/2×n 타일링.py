
N = int(input())

dp = []

dp.append(0)
dp.append(1)
dp.append(2)

if N==1:
    print(dp[N])
elif N==2:
    print(dp[N])
else:
    for i in range(3, N+1):
        dp.append(dp[i-2]+dp[i-1])

    print(dp[-1]%10007)