"""
3
12 10 4
"""
import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())
scvs = list(map(int, input().split(" ")))

damages = [9, 3, 1]
dam_cases = list(permutations(damages, 3))

from collections import deque

dq = deque([])
dq.appendleft(scvs)
res = 0

visit_dict = dict()


while dq:
    nxt_storage = []
    res += 1
    
    for scv_case_idx in range(len(dq)):
        cur_scvs = dq.pop() # (12, 9, 3)
        if len(cur_scvs) == 0:
            print(res-1)
            sys.exit()

        # 현재 scv에 대해 대미지 케이스 적용
        for dams in dam_cases:
            nxt_scvs = []
            for i in range(len(cur_scvs)):
                cur_scv = cur_scvs[i] # 12
                cur_dam = dams[i] # dams: (9, 3, 1)
                nxt_hp = cur_scv - cur_dam
                if nxt_hp > 0:
                    nxt_scvs.append(nxt_hp)
            
            if not visit_dict.get(tuple(nxt_scvs), False): # 방문하지 않았을 때만 간다
                visit_dict[tuple(nxt_scvs)] = True
                nxt_storage.append(nxt_scvs)
    dq = deque(nxt_storage)

print(res)