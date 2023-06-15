N = int(input())
res = 0
cols = [0] * N  # 각 열에 퀸이 놓였는지를 기록하는 배열
diags1 = [0] * (2*N-1)  # / 방향의 대각선에 퀸이 놓였는지를 기록하는 배열
diags2 = [0] * (2*N-1)  # \ 방향의 대각선에 퀸이 놓였는지를 기록하는 배열


def dfs(x):
    global res
    if x == N:
        res += 1
        return
    for y in range(N):
        if cols[y] or diags1[x+y] or diags2[x-y+N-1]:
            continue
        cols[y] = diags1[x+y] = diags2[x-y+N-1] = 1
        dfs(x+1)
        cols[y] = diags1[x+y] = diags2[x-y+N-1] = 0  # 퀸을 빼고 다음 위치로 이동


dfs(0)

print(res)
