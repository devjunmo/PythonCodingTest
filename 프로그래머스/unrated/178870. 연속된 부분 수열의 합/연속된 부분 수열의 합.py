def solution(sequence, k):
    
    if sequence[0] == k:
        return [0, 0]
    
    fp = 1
    bp = 0
    
    seq_len = len(sequence)
    cur_min_fp = 2000000
    cur_min_bp = -1
    tmp_sum = sequence[0]
    # 뒤에꺼가 끝에 도착하면 끝내기
    while fp <= seq_len-1:
        if sequence[fp] > k:
            break
        
        tmp_sum += sequence[fp] # 프론트 포인터가 한칸 가면 sum에 더하기
        if tmp_sum == k and (fp - bp) < (cur_min_fp - cur_min_bp):
            cur_min_fp = fp
            cur_min_bp = bp

        while tmp_sum > k:
            # 이동하기전 차감하고
            tmp_sum -= sequence[bp]
            # 이동한다
            bp += 1     
        if tmp_sum == k and (fp - bp) < (cur_min_fp - cur_min_bp):
            cur_min_fp = fp
            cur_min_bp = bp
        # bp가 끝까지 왔다면 끝낸다
        if bp == seq_len-1:
            break
        fp += 1
    
    
    answer = [cur_min_bp, cur_min_fp]
    return answer