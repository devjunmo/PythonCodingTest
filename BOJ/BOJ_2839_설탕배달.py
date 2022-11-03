N = int(input())

cnt = 0

while True:

    if N % 5 == 0:
        res = cnt + (N // 5)
        print(res)
        break

    else:
        N -= 3
        cnt += 1

    if N == 0:
        print(cnt)
        break

    if N < 0:
        print(-1)
        break
