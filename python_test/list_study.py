"""
참고 링크

# https://wikidocs.net/14
# https://codingpractices.tistory.com/50?category=1026198

"""


# 2차원 리스트 생성
n = 5; m = 4
lst2 = [[0] * m for _ in range(n)]
print(lst2)

"""
함수들

append
sort / reverse / index / insert / remove / pop / count / extend
"""

a = [1, 2, 3]
print(a)

# 리스트에 요소 추가(append)
a.append(4)
print(a)


# 리스트 정렬(sort)
print('리스트 정렬(sort)')
a = [1, 4, 3, 2]
a.sort()
print(a)

# 리스트 뒤집기(reverse)
print('리스트 뒤집기(reverse)')
a = ['a', 'c', 'b']
a.reverse()
print(a)


# 특정 값에 대한 위치 반환(index)
print('특정 값에 대한 위치 반환(index)')
a = [1,2,2,3]
print(a.index(2)) # 1 <- 시작부 하나를 리턴


# 리스트에 요소 삽입(insert) -에 -를
print('리스트에 요소 삽입(insert) -에 -를')
a = [1, 2, 3]
a.insert(0, 4)
print(a)


# 리스트 요소 제거(remove): 리스트에서 첫 번째로 나오는 x를 삭제
print('리스트 요소 제거(remove): 리스트에서 첫 번째로 나오는 x를 삭제')

a = [1, 2, 3, 1, 2, 3]
a.remove(3) # 없으면 ValueError
print(a)

# 리스트 요소 끄집어내기(pop) - 끝에꺼 외치고 삭제
print('리스트 요소 끄집어내기(pop) - 외치고 삭제')

a = [1,2,3]
print(a)
print(a.pop()) # 디폴트는 마지막 요소
print(a)

print(a.pop(0)) # 특정 인덱스 지정 가능
print(a)


# 리스트에 포함된 요소 x의 개수 세기(count)
print('# 리스트에 포함된 요소 x의 개수 세기(count)')
a = [1,2,3,1]
print(a.count(1))


# 리스트 확장(extend)
print('리스트 확장(extend)')
a = [1,2,3]
a.extend([4,5])
print(a)

print(a + [6,7,8]) # 이거랑 동일한 효과


# zip() : 동일한 갯수로 이루어진 데이터 묶기
print(zip([1,2,3], [3,2,1])) # <zip object at 0x0000025633803640>
print(list(zip([1,2,3], [3,2,1]))) # [(1, 3), (2, 2), (3, 1)] // 각 요소가 튜플로 묶여있음

for i in zip([1,2,3], [3,2,1]):
    print(i) # 튜플


# 원소간 합

res = [sum(tup)for tup in zip([1,2,3], [4,5,6])]
print(res)




# 리스트 초기화

my_arr = [[0]] * 5
print(my_arr)

my_arr[0] = [1,2]
print(my_arr)


# list swap

swap_lst = [1, 2, 3, 4]

swap_lst[1], swap_lst[2] = swap_lst[2], swap_lst[1]
print(swap_lst)

if 100:
    print("?")


# count2

arr = [[1, 2, 3],[1, 2, 2],[1, 2, 3]]
print(arr.count(1)) # 0
print(arr[0].count(1)) # 1

print('gi')
print(arr[0][0])

from collections import Counter

ct = Counter([1,2,3])
ct.get((1))