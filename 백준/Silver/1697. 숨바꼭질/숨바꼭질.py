# 5 17
NK = list(map(int, input().split(" ")))
N = NK[0]
K = NK[1]

MAXVAL = 100000

lst = [-1] * (MAXVAL + 1)

from collections import deque

dq = deque([])

dq.appendleft(N)
lst[N] = 0

while len(dq) != 0:
    cur_x = dq.pop()
    x1 = cur_x - 1
    x2 = cur_x + 1
    x3 = cur_x * 2
    
    xs = [x1, x2, x3]
    for x in xs:
        # x가 정상범위 이면서 -1일때 cur_x의 값에 + 1
        if 0<=x<=MAXVAL and lst[x] == -1:
            lst[x] = lst[cur_x] + 1
            dq.appendleft(x)

print(lst[K])