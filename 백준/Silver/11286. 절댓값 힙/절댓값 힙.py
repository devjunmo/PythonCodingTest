

import heapq, sys

N = int(input())

pq = []

for _ in range(N):
    cur_n = int(sys.stdin.readline())
    if cur_n == 0:
        # pop
        if not pq:
            print(0)
        else:
            print(heapq.heappop(pq)[1])
    else:
        # push
        heapq.heappush(pq, (abs(cur_n), cur_n))