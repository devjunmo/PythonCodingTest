import sys, heapq

N = int(sys.stdin.readline())


hq = []

for _ in range(N):
    cur_cmd = int(sys.stdin.readline())
    if cur_cmd == 0:
        if hq:
            print(heapq.heappop(hq))
        else:
            print(0)
    else:
        heapq.heappush(hq, cur_cmd)
