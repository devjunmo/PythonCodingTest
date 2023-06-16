"""
정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.

2를 곱한다.
1을 수의 가장 오른쪽에 추가한다.
A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.

첫째 줄에 A, B (1 ≤ A < B ≤ 10^9)가 주어진다.
A를 B로 바꾸는데 필요한 연산의 최솟값에 1을 더한 값을 출력한다
만들 수 없는 경우에는 -1을 출력한다

dict -> key = 숫자, value = bool

2 162
2 → 4 → 8 → 81 → 162

B에서.. 경우의 수 최대 두개가 나와..
1. *2
2. 꼬다리가 1 더하기

그래서, 무한루프 돌면서 현재 결과 값이 A보다 작다면 break임
만약 현재 결과값이 A와 같다면 cnt 리턴, 그렇지 않다면 -1 리턴
"""
import sys
from collections import defaultdict, deque


A, B = list(map(int, input().split(" ")))
cnt = 1
vis = defaultdict(bool)


dq = deque([A])
vis[A] = True

while dq:
    cnt += 1
    tmp_lst = []
    for cur_num in dq:
        nxt_num1 = (cur_num * 10) + 1
        if nxt_num1 == B:
            print(cnt)
            exit()

        if nxt_num1 < B:
            if not vis[nxt_num1]:
                vis[nxt_num1] = True
                # dq.appendleft(nxt_num1)
                tmp_lst.append(nxt_num1)

        nxt_num2 = int(cur_num * 2)
        if nxt_num2 == B:
            print(cnt)
            exit()

        if nxt_num2 < B:
            if not vis[nxt_num2]:
                vis[nxt_num2] = True
                # dq.appendleft(nxt_num2)
                tmp_lst.append(nxt_num2)

    dq = deque(tmp_lst)

    # cur_num = dq.pop()
    # print(cur_num)



print(-1)