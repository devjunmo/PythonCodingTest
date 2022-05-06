# 10 -> 1 2 5 10
n = 10
res = []

for i in range(n):
    num = i+1
    if n % num == 0:
        res.append(num)

res = sorted(res)

for i in res:
    print(i, end = ' ')