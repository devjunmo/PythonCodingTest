case_num = int(input())

for c_num in range(1, case_num+1):

    input_lst = list(map(int, input().split()))

    sum_val = sum(input_lst)
    ln = len(input_lst)

    print(f'#{c_num} {int(round(sum_val/ln, 0))}')