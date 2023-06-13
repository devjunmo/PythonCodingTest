
"""
배열에 자연수 x를 넣는다.
배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.
"""

import heapq
import sys

input = sys.stdin.readline

N = int(input())

pq = []

for _ in range(N):
    x = int(input())

    if x > 0:
        heapq.heappush(pq, -x)
    else:
        if not pq:
            print(0)
        else:
            v = heapq.heappop(pq)
            print(-v)

            