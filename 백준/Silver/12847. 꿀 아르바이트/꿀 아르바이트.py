import sys
input = sys.stdin.readline
n, m = list(map(int, input().split(" ")))

pay_lst = list(map(int, input().split(" ")))

max_val = -1
tmp_sum = 0

st_idx = 0
ed_idx = st_idx + m - 1

# 최초 범위 구간 합 계산
for i in range(st_idx, ed_idx + 1):
    tmp_sum += pay_lst[i]

max_val = tmp_sum

# 윈도우를 한칸씩 진행시키며 tmp_sum 갱신하고, max_val보다 클 경우 max_val 갱신
st_idx += 1
ed_idx += 1

while(ed_idx < n):
    # tmp_sum 갱신
    tmp_sum -= pay_lst[st_idx-1]
    tmp_sum += pay_lst[ed_idx]

    max_val = max(max_val, tmp_sum)

    # 진행
    st_idx += 1
    ed_idx += 1

print(max_val)