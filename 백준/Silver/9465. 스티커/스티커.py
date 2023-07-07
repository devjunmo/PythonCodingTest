import sys

input = sys.stdin.readline

T = int(input())

for tc in range(T):
    n = int(input())
    
    input_lst = []
    dp = [[0] * n for _ in range(2)]
    
    input_lst.append(list(map(int, input().split(" "))))
    input_lst.append(list(map(int, input().split(" "))))

    dp[0][0] = input_lst[0][0]
    dp[1][0] = input_lst[1][0]

    for i in range(1, n):
        dp[0][i] = max(input_lst[0][i] + dp[1][i-1], dp[0][i-1])
        dp[1][i] = max(input_lst[1][i] + dp[0][i-1], dp[1][i-1])


    max_val = -1
    for i in range(2):
        for j in range(n):
            max_val = max(max_val, dp[i][j])
    
    print(max_val)