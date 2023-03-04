
input_count = int(input())

input_lst = []

for i in range(input_count):
    input_lst.append(i+1)

input_lst = list(map(str, input_lst))

res = []

for input_comp in input_lst:
    buffer_lst = []
    for comp in input_comp:
        if comp in ['3', '6', '9']:
            buffer_lst.append('-')
        else:
            buffer_lst.append(comp)

    clap_cnt = buffer_lst.count('-')
    if clap_cnt != 0:
        res.append('-'*clap_cnt)
    else:
        res.append("".join(buffer_lst))

for ans in res:
    print(ans, end=' ')




















