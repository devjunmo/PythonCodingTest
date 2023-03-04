
case_num = int(input())

for c_num in range(case_num):

    tri_n = int(input())
    tri_lst = [[0]*20 for _ in range(tri_n)]

    tri_lst[0][1] = 1

    for tri_row in range(1, tri_n):
        tri_lst[tri_row][tri_row+1] = 1
        for i in range(tri_row, 0, -1):
            tri_lst[tri_row][i] = tri_lst[tri_row-1][i] + tri_lst[tri_row-1][i-1]

    print(f'#{c_num+1}')
    for i in range(tri_n):
        print(" ".join(map(str, tri_lst[i][1:i+2])))




