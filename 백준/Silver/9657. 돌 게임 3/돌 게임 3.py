
N = int(input())

ans_lst = [1] * 1001 # 1일때 SK, -1일때 CY

ans_lst[2] = -1
ans_lst[3] = 1
ans_lst[4] = 1

for i in range(5, 1001):
    tmp_lst = []
    
    a = i-1
    b = i-3
    c = i-4
    
    # 상근이 하나라도 있으면
    if ans_lst[a] == -1 or ans_lst[b] == -1 or ans_lst[c] == -1:
        ans_lst[i] = 1
    else:
        ans_lst[i] = -1


if ans_lst[N] == 1:
    print('SK')
else:
    print('CY')
