

test_arr = [[1,2,3], [4,5,6], [7,8,9]]

[print(arr) for arr in test_arr]

zip(*test_arr)
list(zip(*test_arr))

t_arr = list(map(list, zip(*test_arr)))

[print(arr) for arr in t_arr]



arr = [1, 2, 3]
arr[1:100]