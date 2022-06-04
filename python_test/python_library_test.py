# https://uni2237.tistory.com/56

"""
1. 내장 함수
"""

res1 = eval("(3+5)*7") # 수학 수식(문자열 형태) 계산 결과 반환
res1 # 56


"""
2. itertools

2.1 permutations (순열): iterable에서 r개의 데이터를 뽑아 일렬로 나열

2.2 combinations (조합): iterable에서 r개의 데이터를 순서 없이 나열

2.3 product (중복 순열): 중복을 허용한 순열

2.4 combinations_with_replacement (중복 조합): 중복을 허용한 조합

2.5 heap 라이브러리: import heapq 하여 heappush로 넣고, heappop으로 뺀다

"""


lst_data = ['A', 'B', 'C']

# 순열로 뽑기
from itertools import permutations
permutations(lst_data, 3) # permuation 객체
res2 = list(permutations(lst_data, 3))
res2 # 리스트 속 튜플로 모든 경우의 수 나열


# 조합으로 뽑기
from itertools import combinations

res3 = list(combinations(lst_data, 2))
res3

long_lst = [i for i in range(1, 100)]
long_lst

res3_1 = list(combinations(long_lst, 3)) # 수가 커지면 터짐
res3_1


# 중복순열(중복 허용 순열)로 뽑기

from itertools import product

res4 = list(product(lst_data, repeat=3))
res4


# 중복조합(중복 허용 조합)으로 뽑기
from itertools import combinations_with_replacement

res5 = list(combinations_with_replacement(lst_data, 2))
res5


# heapq : 디폴트 = 최소 힙

import heapq


def heapsort(my_iter):
    heap_ds = []
    res = []

    # 힙에 데이터 삽입
    for val in my_iter:
        heapq.heappush(heap_ds, val)

    print(heap_ds)

    # 힙의 모든 원소 꺼내기
    for _ in range(len(heap_ds)):
        res.append(heapq.heappop(heap_ds))

    return res


print(heapsort([2,1,3,0,5,4]))


# 최대 힙
def heapsort_max(my_iter):
    heap_ds = []
    res = []

    # 힙에 데이터 삽입
    for val in my_iter:
        heapq.heappush(heap_ds, -val) # 원소에 마이너스 붙이기

    print(heap_ds)

    # 힙의 모든 원소 꺼내기
    for _ in range(len(heap_ds)):
        res.append(-heapq.heappop(heap_ds)) # 원소에 마이너스 붙이기

    return res

print(heapsort_max([2,1,3,0,5,4]))


from collections import deque

dq = deque([1,2,3,4,5]) # 리스트를 넣어줘서 초기화
dq # deque([1, 2, 3, 4, 5])
list(dq) # [1, 2, 3, 4, 5]

dq.append(100)
dq
dq.appendleft(200)
dq # deque([200, 1, 2, 3, 4, 5, 100])

dq.pop() # 100
dq # deque([200, 1, 2, 3, 4, 5])
dq.popleft() # 200
dq # deque([1, 2, 3, 4, 5])


from collections import Counter

counter = Counter(['r','b','r','b','g','b'])
counter.get('r')
counter['r']

print(counter['b']) # 'b' 등장횟수, 답: 3
print(counter['o']) # 0
print(dict(counter)) # {'r':2, 'b':3, 'g':1}


import math

max(math.inf, 1 ,2, 3)
type(math.inf)

print(math.factorial(5))
print(math.sqrt(7))
print(math.gcd(21, 14))
print(math.pi)
print(math.e)











