case_num = int(input())

# N_max = 100

for case_num in range(1, case_num+1):

    N, D = list(map(int, input().split()))

    # garden_lst = [0] * N_max

    start_point = 1
    sprint_count = 0

    while True:

        star_point = start_point + D
        sprint_count += 1

        end_point = star_point + D

        if end_point < N:
            start_point = end_point + 1

        else:
            break

    print(f'#{case_num} {sprint_count}')
