
from itertools import combinations

test_set = {(7, 3), (3, 7)}
print(test_set) # {(3, 7), (7, 3)}

test_set_sorted = {tuple(sorted([7, 3])), tuple(sorted([3, 7]))}
print(test_set_sorted) # {(3, 7)}


# 원소 추가
test_set.add(1)
test_set


# 여러 원소 추가
test_set.update([1,2,3,4])
test_set


# 원소 제거
test_set.remove(1)
test_set
test_set.remove(1) # 없으면 키에러
test_set.discard(1) # 없어도 키에러 x


# 합연산
set2 = {2, 100, 200, 300}
union_set = test_set | set2
union_set


# 교집합
test_set & set2
