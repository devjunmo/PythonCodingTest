case_num = int(input())

# test_str = input()
# test_str = 'EXOEXOEXOEXOEXOEXOEXOEXOEXOEXO'


MAX_FRAGMENT = 10

p_pointer = 0
same_length = 0
flag = False

for c_num in range(case_num):
    num = c_num + 1
    test_str = input()
    for frag_case in range(MAX_FRAGMENT):  # 0 ~ 9  // 1~9
        next_ptr = frag_case+1
        if flag is True:
            flag = False
            break
        if test_str[p_pointer] == test_str[next_ptr]:
            for i in range(next_ptr):
                fst_ptr = i
                late_ptr = i + next_ptr
                if test_str[fst_ptr] == test_str[late_ptr]:
                    same_length += 1
                    if same_length == next_ptr:
                        flag = True
                        print(f'#{num} {same_length}')
                        same_length = 0
                        break
                else:
                    same_length = 0
                    break





