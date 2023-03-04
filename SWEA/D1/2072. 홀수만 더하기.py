
res_dict = dict()

case_len = int(input())

for i in range(case_len):
    num = i+1
    input_lst = list(map(int, input().split()))
    odd_num_lst = [k for k in input_lst if k % 2 != 0]
    res_dict[num] = odd_num_lst

for i in range(case_len):
    num = i + 1
    print(f'#{num} {sum(res_dict[num])}')
