
T=8
tmp = 0
for test_case in range(1, T + 1):
    if tmp == 0:
        print(1, end=" ")
        tmp = 1

    print(tmp * 2, end=" ")
    tmp *= 2
