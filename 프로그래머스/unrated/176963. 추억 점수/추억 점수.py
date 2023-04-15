def solution(name, yearning, photo):
    answer = []
    for p in photo:
        tmp_sum = 0
        for i in p:
            tmp_idx = 0
            for j in name:
                if i == j:
                    tmp_sum += yearning[tmp_idx]
                    break
                tmp_idx += 1
        answer.append(tmp_sum)
    return answer