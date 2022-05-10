# <부족한 기초 문법 채우기>
# 나동빈 선생님 강의 참고
# https://www.youtube.com/watch?v=m-9pAwq1o3w&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=1


# 1. 자료형
print('########################')
print("1. 자료형")
print('########################')

## 1.1 지수승 표현

print('2e10 = ', 2e10)  # 유효 숫자 e 지수승
print('int(2e10) = ', int(2e10))

## 1.2 실수형 정밀도 문제
print('0.9==0.3+0.6 = ', 0.9==0.3+0.6)  # False --> 실수간 비교시 round 같은 거로 보완
print('0.9==round(0.3+0.6, 1) = ', 0.9==round(0.3+0.6, 1))  # True
print('4/2 = ', 4/2)  # 나누기는 실수형 으로 리턴됨
print('4%2 = ', 4%2)  # 나머지 연산자는 정수 리턴
print('4//2 = ', 4//2)  # 몫 연산자는 정수 리턴
print('2**2 = ', 2**2)  # 거듭제곱
print('2**0.5 = ', 2**0.5)  # 제곱근

## 1.3 리스트 자료형

print('[0]*10 = ', [0]*10) # 리스트 초기화
print('[1,2,3,4,5][1:3] = ', [1,2,3,4,5][0:3])
print('[i for i in [1, 2, 3] if i == 1] ->', [i for i in [1, 2, 3] if i == 1]) # 리스트 컴프리핸션의 리턴 타입은 리스트다.
print('[[0]*4 for _ in range(5)]  -> ', [[0]*4 for _ in range(5)]) # 5x4 형태의 2차원 리스트 초기화
print('[1,1,2,5].count(1) = ', [1,1,2,5].count(1)) # 특정 값 몇개인지 출력
# 리스트 요소 중 특정 값 모두 제거
print('[i for i in [1,2,3,4,5,5,5] if i not in {3, 4}]  -> ', [i for i in [1,2,3,4,5,5,5] if i not in {3, 4}])


## 1.4 스트링 자료형
print("'abcd'[0:2] = ", 'abcd'[0:2]) # 슬라이싱 가능
print("a[0] = 'A'는 불가. Immutable 특성")


## 1.5 튜플 자료형
print('Key값 같이 데이터가 바뀌면 안될 때 튜플 쓰자')

## 1.6 딕셔너리 자료형
print('keys, values 함수!')

## 1.7 set 자료형
print('{1, 2, 3, 4} | {3, 4, 5, 6}', {1, 2, 3, 4} | {3, 4, 5, 6}) # 합집합
print('{1, 2, 3, 4} & {3, 4, 5, 6}', {1, 2, 3, 4} & {3, 4, 5, 6}) # 교집합
print('{1, 2, 3, 4} - {3, 4, 5, 6}', {1, 2, 3, 4} - {3, 4, 5, 6}) # 차집합
print('add, update(여러개를 리스트로 add), remove 함수 사용 가능')


# 2. 입출력
print('########################')
print("2. 입출력")
print('########################')

# 2.1 input(), map()

# n = int(input()) # 데이터 갯수 입력
# print('n =', n)
#
# my_data = list(map(int, input().split())) # '공백' 기준이 디폴트
# print('my_data = ', my_data)
#
# a, b, c = list(map(int, input().split()))
# print(a, b, c)

# 2.2 많이, 빠르게 입력 받기 -> System library (sys)
##  sys.stdin.readline() & rstrip()
# 이진탐색, 정렬, 그래프 관련

# import sys
# data = sys.stdin.readline().rstrip().split(' ')
# print(data)
#
# ## 문자열 n줄 입력받아 리스트에 저장
# n = int(sys.stdin.readline())
# data = [sys.stdin.readline().strip() for i in range(n)]
# print(data)
#
# print('adsf'.strip())


# 3. 조건문

if True and True:
    print('hi')

print('a' in ['a', 1, 2])
print('a' not in ['a', 1, 2])

if 1 < 16 < 20:
    print('16')



# 4. 여러개의 반환값 - 패킹과 언패킹
# return에 var1, var2, var3로 리턴하고
# a, b, c = myFun() 요렇게 받기

print((lambda a, b: a+b)(3, 7)) # (lambda 입력:리턴)(넣을 인자)

array = [('B', 60), ('A', 50), ('C', 70)]
print(sorted(array, key=lambda x: x[1]))  # 정렬 기준을 람다로 표현

print([1,2]+[3,4]) # [1, 2, 3, 4]
print(list(map(lambda a, b:a+b, [1,2], [3, 4]))) # [4, 6]



# 5. 자주 사용되는 내장함수

res = eval("(3+5)*7")
print(res)
print((3+5)*7)

print(sorted([1, 3, 5, 2], reverse=True))


























