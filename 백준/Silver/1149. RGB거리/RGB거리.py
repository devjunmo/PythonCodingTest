N = int(input())

# a = [[0]*3] * (N + 10)
s = []

for _ in range(N+10):
    s.append([0]*3)


# dp 테이블 채우기
for i in range(N):
    # RGB 코스트 리스트
    rgb_cost_list = list(map(int, input().split(" ")))
    R = rgb_cost_list[0]
    G = rgb_cost_list[1]
    B = rgb_cost_list[2]
    
    # 초기값 대입 
    if i == 0:
        s[i][0] = R
        s[i][1] = G
        s[i][2] = B
    # 2항부터
    else:
        # 현재 R을 선택
        s[i][0] = rgb_cost_list[0] + min(s[i-1][1], s[i-1][2])
        # 현재 G을 선택
        s[i][1] = rgb_cost_list[1] + min(s[i-1][0], s[i-1][2])
        # 현재 B을 선택
        s[i][2] = rgb_cost_list[2] + min(s[i-1][0], s[i-1][1])


print(min(s[N-1]))