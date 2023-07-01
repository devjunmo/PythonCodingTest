N, M = list(map(int, input().split(" ")))
input_lst = list(map(int, input().split(" ")))

input_lst.sort()
res_lst = []


def dfs(st_idx):
    if len(res_lst) == M:
        print(*res_lst)
        return

    tmp = 0
    for i in range(st_idx, N):
        if tmp != input_lst[i]:
            res_lst.append(input_lst[i])
            tmp = input_lst[i]
            dfs(i)
            res_lst.pop()


dfs(0)
