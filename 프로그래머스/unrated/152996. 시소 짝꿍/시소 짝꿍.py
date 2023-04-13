from collections import Counter
from itertools import combinations

def solution(weights):
    cnts = Counter(weights)
    # print(cnts)
    val_lst = []
    cnt_lst = []
    
    for v in cnts:
        val_lst.append(v)
        cnt_lst.append(cnts[v])
    
    answer = 0
    weight_len = len(cnts)
    
    for i in range(weight_len):
        if cnt_lst[i] > 1:
            #  카운트 두개 이상이면 nC2 추가
            # answer += len(list(combinations(range(cnt_lst[i]), 2)))
            answer += (int)((cnt_lst[i] * (cnt_lst[i]-1)))/2
        for j in range(i+1, weight_len):
            
            set1 = set([val_lst[i] * 2, val_lst[i] * 3, val_lst[i] * 4])
            set2 = set([val_lst[j] * 2, val_lst[j] * 3, val_lst[j] * 4])
            if set1 & set2:
                answer += cnt_lst[i] * cnt_lst[j]
    return answer










