import sys
import time

# 결론: 
# 입력시 sys.stdin.readline() 쓰고
# 출력시 걍 print() 쓰자

# Generate a list of 1 million numbers
numbers = list(range(1000000))


# # Test using sys.stdout.write()
# start_time = time.time()
# sys.stdout.write(' '.join(map(str, numbers)))
# end_time = time.time()
# write_time = end_time - start_time
# print("sys.stdout.write() time: ", write_time) # (백만) 1.6875231266021729 (천만) 17.109848737716675




# start_time = time.time()
# print(' '.join(map(str, numbers)))
# end_time = time.time()
# print_time = end_time - start_time
# print("print() time: ", print_time) # print() time:  1.76680588722229



# start_time = time.time()
# print('\n'.join(map(str, numbers)))
# end_time = time.time()
# print_time = end_time - start_time
# print("print() time: ", print_time) # print() time:  3.152168035507202



# 얘가 더 느림 
# # Use a list comprehension to append '\n' to every element
# numbers_with_newline = [str(number) + '\n' for number in numbers]

# start_time = time.time()
# print(' '.join(numbers_with_newline))
# end_time = time.time()

# print_time = end_time - start_time
# print("print() time: ", print_time) # (100만개) print() time:  3.4491641521453857

