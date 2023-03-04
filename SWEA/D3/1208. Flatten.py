case_num = 10


def dump():
    max_idx = box_lst.index(max(box_lst))
    min_idx = box_lst.index(min(box_lst))

    box_lst[max_idx] -= 1
    box_lst[min_idx] += 1

    max_idx = box_lst.index(max(box_lst))
    min_idx = box_lst.index(min(box_lst))

    if box_lst[max_idx] - box_lst[min_idx] <= 1:
        return True

    return False


for c_mum in range(1, case_num+1):
    dump_cnt = int(input())

    box_lst = list(map(int, input().split()))

    for _ in range(dump_cnt):
        if dump():
            break

    print(f'#{c_mum} {box_lst[box_lst.index(max(box_lst))] - box_lst[box_lst.index(min(box_lst))]}')

