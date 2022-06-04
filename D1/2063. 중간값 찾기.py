
N = int(input())

input_lst = list(map(int, input().split()))
print(input_lst)

sort_lst = sorted(input_lst)

print(sort_lst[int(N/2)])