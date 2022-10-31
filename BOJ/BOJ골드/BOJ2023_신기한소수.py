N = int(input())

res = []


def is_prime_num(input_num):
    for n in range(2, int(input_num**0.5)+1):
        if input_num % n == 0:
            # 나누어 떨어지면
            return False  # 소수가 아니다
        else:
            continue  # 담꺼 본다
    return True  # 끝까지 안나누어 떨어지면 소수다


# for num in range(2*10**(N-1), (10**N)):  # num = N 범위에 해당 하는 숫자들
#
#     trigger = True
#
#     # 7 -> // 10 ^ (N - 1)
#     # 73 -> // 10 ^ (N - 2)
#     # 733 -> // 10 ^ (N - 3)
#     # 7331 -> // 10 ^ (N - 4)  -> () 부분이 통째로 pos
#     for pos in range(N-1, -1, -1):
#         cur_num = int(num // (10**pos))
#
#         if not is_prime_num(cur_num):  # 중간 놈이 소수가 아니면
#             trigger = False  # trigger 끈다
#             break  # 현재 num 버린다
#
#     if trigger:  # 신기한 소수면
#         res.append(num)


def dfs(cnt, cur_num):
    if cnt == N-1:
        res.append(cur_num)

    # 가능한 모든 수에 대해 생각
    for i in range(10):
        tmp_num = 10 * cur_num + i
        if is_prime_num(tmp_num):
            dfs(cnt+1, tmp_num)
        else:
            continue


dfs(0, 2)
dfs(0, 3)
dfs(0, 5)
dfs(0, 7)

for i in res:
    print(i)








