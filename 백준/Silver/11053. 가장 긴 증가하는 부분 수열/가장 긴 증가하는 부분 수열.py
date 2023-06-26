N = int(input())

input_lst = list(map(int, input().split(" ")))

dp_lst = [1] * len(input_lst)
# dp_lst[0] = 1  # 초항 입력

for i in range(1, len(input_lst)):
    # print(dp_lst)
    # 0번째부터 i번째까지 중 현재 값보다 작은놈의 dp lst 값의 최대값을 가져온다
    cur_max = 0
    for j in range(i):
        if input_lst[j] < input_lst[i]:
            cur_max = max(cur_max, dp_lst[j])
    # 구한 값에 + 1한 값을 현재 dp_lst 순번에 넣는다
    dp_lst[i] = cur_max + 1

print(max(dp_lst))
