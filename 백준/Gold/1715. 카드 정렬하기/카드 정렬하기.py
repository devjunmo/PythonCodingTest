"""
3
10
20
40
"""

import sys, heapq

N = int(input())

hq = [] # len = N

for _ in range(N):
    cur_num = int(sys.stdin.readline())
    heapq.heappush(hq, cur_num)

ans = 0

while len(hq) > 1:
    x1 = heapq.heappop(hq)
    x2 = heapq.heappop(hq)
    ans += x1+x2
    heapq.heappush(hq, x1+x2)

print(ans)