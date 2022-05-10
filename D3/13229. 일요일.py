case_num = int(input())

d_dict = {
    "MON":1,
    "TUE":2,
    "WED":3,
    "THU":4,
    "FRI":5,
    "SAT":6,
    "SUN":7
}

for c_num in range(1, case_num+1):

    input_str = input()
    remain_day = d_dict["SUN"] - d_dict[input_str]

    if remain_day == 0:
        remain_day = 7

    print(f'#{c_num} {remain_day}')