N, M = list(map(int, input().split(" ")))
input_lst = list(map(int, input().split(" ")))
input_lst.sort()
res = []

def dfs(st_idx):
    if len(res) == M:
        print(*res)
        return

    for i in range(st_idx, N):
        res.append(input_lst[i])
        dfs(i)
        res.pop()

dfs(0)


