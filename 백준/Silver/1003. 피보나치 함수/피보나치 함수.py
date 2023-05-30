"""
3
0
1
3
"""

# fib(0) = 0  (1, 0)
# fib(1) = 1  (0, 1)
# f2 = f1 + f0  (1, 1)
# f3 = f2 + f1  = f1 + f0 + f1 = (1, 2)
# f4 = f3 + f2 = [f2 + f1] + [f1 + f0] = [f1 + f0] + f1 + f1 + f0 = (2, 3)

import sys
input = sys.stdin.readline
from collections import defaultdict

T = int(input())
int_dict = defaultdict(tuple)

int_dict[0] = (1, 0)
int_dict[1] = (0, 1)

for _ in range(T):
    N = int(input())
    for i in range(2, N+1):
        int_dict[i] = tuple(map(sum, zip(int_dict[i-1], int_dict[i-2])))
    print(*int_dict[N])

