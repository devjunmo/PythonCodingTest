
# 22220228

case_num = int(input())
day_dict = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
err = -1

for i in range(case_num):
    num = i+1
    input_num_lst = []
    for j in input():
        input_num_lst.append(j)
    print(input_num_lst)

    year = input_num_lst[0:4]
    month = input_num_lst[4:6]
    day = input_num_lst[6:8]

    year_str = ("".join(year))
    month_str = ("".join(month))
    day_str = ("".join(day))

    year = int("".join(year))
    month = int("".join(month))
    day = int("".join(day))

    if not 1 <= month <= 12:
        print(f'#{num} {err}')
    elif day <= 0 or day > day_dict[month]:
        print(f'#{num} {err}')
    else:
        print(f'#{num} {year_str}/{month_str}/{day_str}')

