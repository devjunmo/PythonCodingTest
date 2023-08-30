import heapq

N = int(input())
ds_vote_cnt = int(input())
etc_vote_cnt_heap = []
res = 0


def check_top_rank():
    # 다솜이가 제일 득표수가 많을 때 끝낸다
    if ds_vote_cnt > -etc_vote_cnt_heap[0]:
        return True
    else:
        return False


for _ in range(1, N):
    num = int(input())
    heapq.heappush(etc_vote_cnt_heap, -num)  # 최대힙

if len(etc_vote_cnt_heap) == 0:
    print(res)
else:
    while True:
        if check_top_rank():
            break

        # etc에서 최대값 가져오기
        etc_max_val = -heapq.heappop(etc_vote_cnt_heap)

        # 다솜 +1, 최대값 -1
        ds_vote_cnt += 1
        etc_max_val -= 1

        # 최대값 다시 힙에 넣기
        if etc_max_val > 0:
            heapq.heappush(etc_vote_cnt_heap, -etc_max_val)

        res += 1

    print(res)

