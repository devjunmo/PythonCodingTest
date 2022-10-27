
# 문제풀이방법: 반복문 + 2방탐색 + 딕셔너리로 방문체크

TC = 10

init_lst_size = 100

# 우 좌
dx = [0, 0]
dy = [1, -1]

for _ in range(1, TC+1):

    c_num = int(input())

    input_lst = [list(map(int, input().split(" ", maxsplit=init_lst_size-1))) for _ in range(init_lst_size)]
    # print(input_lst)

    cur_y = input_lst[-1].index(2)  # 도착 점 부터 거꾸로 올라 가려고
    cur_x = init_lst_size - 1

    vis_dict = dict()

    while cur_x > 0:
        # 방문 체크
        vis_dict[(cur_x, cur_y)] = True

        is_side = False
        for i in range(2):  # 우, 좌 탐색
            # nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            # 방문하지 않았으면서 next가 정상범위일 때
            if not vis_dict.setdefault((cur_x, ny), False) and (0 <= ny < init_lst_size):
                # 사이드일때
                if input_lst[cur_x][ny] == 1:
                    cur_y = ny  # cur_y 갱신
                    is_side = True
                # 사이드 아닐때
                else:
                    continue

                break  # 좌우에 1이 있다면 글로 가고 좌우 탐색 break

        if is_side:
            continue  # 옆으로 간다면 위로 안올라간다

        cur_x -= 1  # 리스트의 한칸을 올라 가는 효과

    print(f'#{c_num} {cur_y}')





