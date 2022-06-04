# https://codechacha.com/ko/python-sorting-dict/ 참고


# Key를 기준으로 정렬 (오름차순)

my_dict = {'c': 3, 'a': 1, 'b': 2, 'e': 1, 'd': 2}

sorted_dict = sorted(my_dict.items())
print(sorted_dict) # 디폴트는 key 기준 오름차순 정렬 됨.
                    # ** 딕셔너리는 깨지고 **, 리스트 속에 튜플 구조로 리턴


# Key를 기준으로 정렬 (내림차순)

# sorted_dict = sorted(my_dict.items(), reverse = True)
# sorted_dict = sorted(my_dict.items(), key = lambda item: item[0], reverse = True)
# sorted_dict = sorted(my_dict, reverse=True) # 이렇게 하면 이상한 값이 리스트로 리턴
sorted_dict = sorted(my_dict.items(), key=lambda x:x[0], reverse=True) # 소팅하려면 item으로 소팅해야하고, 결과는 딕셔너리가 깨짐
print(sorted_dict)


# Value를 기준으로 정렬 (오름차순)
print(my_dict.items())  # dict_items([('c', 3), ('a', 1), ('b', 2), ('e', 1), ('d', 2)])
sorted_dict = sorted(my_dict.items(), key=lambda x:x[1]) # x[1]은 items객체상에서 value 자리에 해당됨
print(sorted_dict)


# Value를 기준으로 정렬 (내림차순)
sorted_dict = sorted(my_dict.items(), key=lambda x:x[1], reverse=True)
print(sorted_dict) # 리스트

print(sorted_dict[0][0])








