case_num = int(input())

for c_num in range(1, case_num+1):

    N = int(input())

    vis_arr = [[False] * N for _ in range(N)]
    ans_arr = [[0] * N for _ in range(N)]

    # print(vis_arr)

    EST = [0, 1]
    SOU = [1, 0]
    WES = [0, -1]
    NTH = [-1, 0]

    cur_num = 1
    cur_x = 0
    cur_y = 0

    while True:

        vis_arr[cur_x][cur_y] = True
        ans_arr[cur_x][cur_y] = cur_num

        # 동
        pc1 = 0
        while True:
            try:
                tmp_cur_x = cur_x + EST[0]
                tmp_cur_y = cur_y + EST[1]
                if vis_arr[tmp_cur_x][tmp_cur_y] is False:
                    cur_num += 1
                    cur_x = cur_x + EST[0]
                    cur_y = cur_y + EST[1]
                    vis_arr[cur_x][cur_y] = True
                    ans_arr[cur_x][cur_y] = cur_num
                    pc1 += 1
                else:
                    break

            except IndexError:
                break
        # print(ans_arr)

        # 남
        pc2 = 0
        while True:
            try:
                tmp_cur_x = cur_x + SOU[0]
                tmp_cur_y = cur_y + SOU[1]
                if vis_arr[tmp_cur_x][tmp_cur_y] is False:
                    cur_num += 1
                    cur_x = cur_x + SOU[0]
                    cur_y = cur_y + SOU[1]
                    vis_arr[cur_x][cur_y] = True
                    ans_arr[cur_x][cur_y] = cur_num
                    pc2 += 1
                else:
                    break

            except IndexError:
                break
        # print(ans_arr)

        # 서
        pc3 = 0
        while True:
            try:
                tmp_cur_x = cur_x + WES[0]
                tmp_cur_y = cur_y + WES[1]

                if tmp_cur_x < 0 or tmp_cur_y < 0:
                    break

                if vis_arr[tmp_cur_x][tmp_cur_y] is False:
                    cur_num += 1
                    cur_x = cur_x + WES[0]
                    cur_y = cur_y + WES[1]
                    vis_arr[cur_x][cur_y] = True
                    ans_arr[cur_x][cur_y] = cur_num
                    pc3 += 1
                else:
                    break

            except IndexError:
                break
        # print(ans_arr)

        # 북
        pc4 = 0
        while True:

            try:
                tmp_cur_x = cur_x + NTH[0]
                tmp_cur_y = cur_y + NTH[1]

                if tmp_cur_x < 0 or tmp_cur_y < 0:
                    break

                if vis_arr[tmp_cur_x][tmp_cur_y] is False:
                    cur_num += 1
                    cur_x = cur_x + NTH[0]
                    cur_y = cur_y + NTH[1]
                    vis_arr[cur_x][cur_y] = True
                    ans_arr[cur_x][cur_y] = cur_num
                    pc4 += 1
                else:
                    break

            except IndexError:
                break

        if pc1 + pc2 + pc3 + pc4 == 0:
            break

    print(f'#{c_num}')

    for k in range(N):
        print(" ".join(map(str, ans_arr[k])))

