# https://wikidocs.net/16 참고


test_dict = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
test_dict2 = {1:100, 3:200, 2:600}


# keys() 함수는 key를 출력한다
print(test_dict.keys())  # dict_keys(['name', 'phone', 'birth'])
print(list(test_dict.keys()))  # ['name', 'phone', 'birth']

# values() 함수는 value를  출력한다
print(test_dict.values())  # dict_values(['pey', '0119993323', '1118'])
print(list(test_dict.values()))  # ['pey', '0119993323', '1118']

# Key, Value 쌍 얻기(items)
print(test_dict.items())  # dict_items([('name', 'pey'), ('phone', '0119993323'), ('birth', '1118')])
print(list(test_dict.items()))

for k, val in test_dict.items():
    print(f'key는 {k}이고, val은 {val}이다.')


# Key로 value 얻기

## 방법1 [] 사용 -> KeyError 발생
print(test_dict['name'])

## 방법2 .get() 사용 -> 없을때는 None 리턴
print(test_dict.get('name')) # pey
print(test_dict.get('no')) # None
print(test_dict.get('no', 2)) # 키가 없을때 디폴트 값 출력 설정


# 해당 Key가 딕셔너리 안에 있는지 조사하기(in)
print('name' in test_dict) # True


# setdeafult() = 키가 없으면 맨 뒤에 추가
test_dict.setdefault('new1', 'my')
test_dict2.setdefault(7, 1)

print(test_dict)
print(test_dict2)


# pop() : 지정된 key값을 제거하며 value를 출력
print(test_dict.pop('new1'))
print(test_dict)


# popitem() -> 맨 끝값 제거하면서 키벨류를 튜플로 리턴
print(test_dict.popitem())
print(test_dict)


# update() -> 두 딕셔너리 합치기
test_dict3 = {100:10, 200:20}
print(test_dict2)
test_dict2.update(test_dict3)
print(test_dict2)


# copy() -> 얕은 복사










