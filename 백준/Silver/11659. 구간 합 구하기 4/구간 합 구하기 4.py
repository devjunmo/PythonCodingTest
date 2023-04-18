N, M = list(map(int, input().split(" ")))
input_lst = list(map(int, input().split(" ")))

res = []  # 결과 저장

# Sum lst 구해 두기 (Sn = Sn-1 + An)  //  S0 = A0
a0 = input_lst[0]
sum_lst = [a0]

for i in range(1, N):
    sum_lst.append(sum_lst[i-1] + input_lst[i])

# 제시된 구간 합 구하기
for _ in range(M):
    start, end = list(map(int, input().split(" ")))
    start -= 1
    end -= 1  # 인덱스 영부터
    if start == 0:
        res.append(sum_lst[end])
    else:
        res.append(sum_lst[end] - sum_lst[start-1])

for r in res:
    print(r)

