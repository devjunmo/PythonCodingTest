
# 그리디 -> 완탐에서 죽음의 냄새가 나면 그리디가 아닐까 의심

TC = int(input())


for cNum in range(1, TC + 1):
    target_lst = list(map(int, input()))
    input_len = len(target_lst)
    init_lst = [0] * input_len

    ans = 0

    for i in range(input_len):
        if target_lst[i] == init_lst[i]:
            continue
        else:
            if target_lst[i] == 0:
                for j in range(i, input_len):
                    init_lst[j] = 0
            elif target_lst[i] == 1:
                for j in range(i, input_len):
                    init_lst[j] = 1
            ans += 1

    print(f"#{cNum} {ans}")
