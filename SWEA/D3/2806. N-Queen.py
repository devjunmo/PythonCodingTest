
"""
바킹독님 알고리즘 강의 해설
https://www.youtube.com/watch?v=Enz2csssTCs&list=PLtqbFd2VIQv4O6D6l9HcD732hdrnYb6CY&index=13

"""

N = int(input())

count = 0

arr = [[True] * N for _ in range(N)]

is_used1 = [False] * 40 # 열을 사용중 인걸 표시
is_used2 = [False] * 40 # 좌하~우상 대각선을 사용중인걸 표시
is_used3 = [False] * 40 # 좌상~우하 대각을 사용중임을 표시


def backTracking(cur):
    global count

    if cur == N:
        count += 1
        return

    for j in range(N):
        if is_used1[j] or is_used2[j+cur] or is_used3[cur-j+N-1]:
            continue

        is_used1[j] = True
        is_used2[j+cur] = True
        is_used3[cur-j+N-1] = True

        backTracking(cur+1)

        is_used1[j] = False
        is_used2[j + cur] = False
        is_used3[cur - j + N - 1] = False


backTracking(0)

print(count)
