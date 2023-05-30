
"""
3 4
ohhenrie
charlie
baesangwook
obama
baesangwook
ohhenrie
clinton
"""

import sys
from collections import defaultdict

input = sys.stdin.readline
N, M = list(map(int, input().split(" ")))

d_int = defaultdict(int)

for i in range(N):
    str = input().rstrip()
    d_int[str] = 1

for i in range(M):
    str = input().rstrip()
    val = d_int[str]
    if val == 1:
        # dict의 값을 2로해
        d_int[str] = val + 1
    else:
        d_int[str] = 1

res = []
for k, v in d_int.items():
    if v > 1:
       res.append(k)

res.sort()

print(len(res))
for r in res:
    print(r)