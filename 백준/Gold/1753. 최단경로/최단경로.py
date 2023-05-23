VE = list(map(int, input().split(" ")))

V = VE[0]
E = VE[1]

K = int(input()) # 시작 정점

import sys

d_lst = [sys.maxsize] * (V+1)

# E개의 줄에 걸쳐 각 간선을 나타내는 세 개의 정수 (u, v, w)가 순서대로 주어진다. 
# u에서 v로 가는 가중치 w인 간선
input_lst = []

for i in range(V+1):
    input_lst.append([])


for i in range(E):
    e_info = list(map(int, sys.stdin.readline().split(" ")))
    st, ed, w = e_info
    # (가중치, 정점) 형태로 
    input_lst[st].append((w, ed))

# print(input_lst)

d_lst[K] = 0 # 출발점

import heapq

pq = []

# 처음 요소 대입

# for tup in input_lst[K]:
#     heapq.heappush(pq, tup)
#     d_lst[tup[1]] = tup[0]

heapq.heappush(pq, (0, K))


while pq:
    cur_tup = heapq.heappop(pq) # (가중치, 정점)
    ce, cv = cur_tup
    if d_lst[cv] == ce:
        for tp in input_lst[cv]:
            ne, nv = tp
            # 기존꺼 보다 작을때만 갱신 후 pq에 넣기
            next_candidate_dist = d_lst[cv] + ne
            if d_lst[nv] > next_candidate_dist:
                d_lst[nv] = next_candidate_dist # 갱신
                heapq.heappush(pq, (next_candidate_dist, nv)) # push

for i in range(1, len(d_lst)):
    if d_lst[i] == sys.maxsize:
        print("INF")
    else:
        print(d_lst[i])