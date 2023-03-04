print('-'*2)


for i in range(0):
    print('jho')
    print(i)

tmp_lst = [1, 2, 3]

print(sum(tmp_lst))
print(max(tmp_lst))

test_tup = (1, 2)
print(test_tup[0])

print('[1][-1] = ', [1][-1])

max_tst = [1, 2, 3, 3, 3]

print(max(max_tst))

print(max_tst.index(max(max_tst))) # 2

t1 = max_tst[:2+1]
print(t1) # [1, 2]
t2 = max_tst[2+1:]
print(t2)

t3 = max_tst[5:]
print(t3)
print(len([])) # 0

max_tst = [1, 2, 3, 3, 3]

max_tmp = max_tst[-1]
print('끝 제외 = ', max_tst[:5-1])

process_tst = [max_tmp - i for i in max_tst[:len(max_tst)-1]]

print(process_tst)

print(int('123'))

print("".join(map(str, [1,2,3])))

print(list(str(1234)))

print(int(1.7))
import math
math.ceil(1.7)