case_num = int(input())

for _ in range(case_num):

    freq_dict = dict()
    cur_case_num = int(input())
    input_lst = list(map(int, input().split()))

    for score in input_lst:
        try:
            tmp_freq = freq_dict[score]
            freq_dict[score] = tmp_freq + 1
        except KeyError:
            freq_dict[score] = 1

    # 딕셔너리를 value 기준으로 소팅
    freq_dict_sorted = sorted(freq_dict.items(), key=lambda x:x[1], reverse=True) # 리스트

    # 리스트 내 튜플 첫번째 요소를 꺼내고, 그녀석에 해당되는 튜플로만 꺼내서 맨 마지막 요소를 출력 해야함
    # 왜냐면 freq대로 내림차순 소팅을 하긴 했는데, key는 오름차순 소팅이 자동 적용되서..

    freq_max_cnt = freq_dict_sorted[0][1]  # key=score : val=freq
    res_lst = []

    for tup in freq_dict_sorted:
        if tup[1] == freq_max_cnt:
            res_lst.append(tup)

    res_lst_sorted = sorted(res_lst, key=lambda x:x[0])
    # print(res_lst_sorted)

    # score: freq이 max인 애만 나왔고, 얘중 끝 key가 max점수임
    print(f'#{cur_case_num} {res_lst_sorted[-1][0]}')


