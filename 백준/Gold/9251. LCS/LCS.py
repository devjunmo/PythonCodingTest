
def lcs(X , Y): 
    m = len(X) 
    n = len(Y) 
  
    dp = [[0]*(n) for i in range(m)] 
  
    for i in range(m): 
        for j in range(n): 
            if i == 0 or j == 0: 
                if X[i] == Y[j]: 
                    dp[i][j] = 1
                elif i > 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i][j-1]
            elif X[i] == Y[j]: 
                dp[i][j] = dp[i-1][j-1]+1
            else: 
                dp[i][j] = max(dp[i-1][j] , dp[i][j-1]) 
  
    return dp[m-1][n-1]

x = input()
y = input()

print(lcs(x, y))