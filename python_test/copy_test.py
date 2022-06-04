# https://justdoit709.tistory.com/100 참고

# 리스트는 mutable 객체

mu_a = [2020, 'year']
mu_b = mu_a
mu_b.append(['hi', 'hello'])

print(mu_a is mu_b) # True (동일 객체임)
print(mu_a) # 언뜻 보면 [2020, 'year'] 출력될것 같지만
            # [2020, 'year', ['hi', 'hello']] 출력

"""
위처럼 mutable 객체를 다른 변수에 추가 하면,
하나의 객체를 두개의 변수가 참조 하고 있는 것일 뿐임.

저렇게 하기 싫고, 각 변수에 객체를 생성해 주고 싶다면?? -> 얕은 복사
"""

mu_a = [2020, ['hi', 'hello']]
mu_b = mu_a.copy()

print(mu_a is mu_b) # False (서로 다른 객체임)

mu_b.append('year')
print(mu_b)  # [2020, ['hi', 'hello'], 'year']
print(mu_a)  # [2020, ['hi', 'hello']]  <- 반영 되지 않음!!


# 얕은 복사의 허점
mu_b[1][1] = 'bye'  # 요소중 mutable 객체를 수정함
print(mu_b)  # [2020, ['hi', 'bye'], 'year']
print(mu_a)  # [2020, ['hi', 'bye']]   // 둘 다 hello에서 bye로 수정됨


"""
얕은 복사의 허점을 보완 한게 깊은 복사.

import copy
"""


# 슬라이싱으로 테스트

test_lst = [1, 2, 3, 4, 5, 6, [1,2,3]]

left = test_lst[:3]
right = test_lst[3:]

print(left) # [1, 2, 3]
print(right) # [4, 5, 6]

left[0] = 10
print(left) # [10, 2, 3]
print(test_lst) # [1, 2, 3, 4, 5, 6]

right[-1][0] = 100
print(test_lst)  # [1, 2, 3, 4, 5, 6, [100, 2, 3]]    // 슬라이싱은 얕은 복사로 돈다














