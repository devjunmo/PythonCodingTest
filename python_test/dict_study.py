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
print(test_dict.get('no')) # 저장 되는건 아님.

# 해당 Key가 딕셔너리 안에 있는지 조사하기(in)
print('name' in test_dict) # True


# setdeafult() = 키가 없으면 맨 뒤에 추가
print('setdefault')
test_dict.setdefault('new1', 'my')
test_dict2.setdefault(7, 1)

print(test_dict)
print(test_dict2)

test_dict3 = dict()

test_dict3.setdefault("k1", [])
test_dict3["k1"].append(100)
test_dict3["k1"].append(200)
test_dict3["k1"]

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



# 딕셔너리 컴프리핸션
# https://ybworld.tistory.com/96 참고

## 1) 이름 리스트를 입력받아 value가 빈 딕셔너리 생성
name = ['YB', 'SW', 'EJ']
dict1 = {r : '-' for r in name}
print(dict1)

## 2) 조건 걸기
name = ['YB', 'SW', 'EJ', 'HJ']
age = [32, 31, 28, 28]

#딕셔너리 생성(name : age)
name_dic = dict(zip(name,age))
name_dic

#나이가 28살인 사람만 딕셔너리로 생성하는 컴프리헨션
dict1 = {k : v for k, v in name_dic.items() if v == 28}
dict1

#이름이 YB인사람만 딕셔너리로
dict2 = {k : v for k, v in name_dic.items() if k =="YB"}
dict2

#key와 value를 서로 바꾸기
dict3 = {v : k for k, v in name_dic.items()}
dict3


## 3) zip으로 바로 딕셔너리 생성하기
name = ['YB', 'SW', 'EJ', 'HJ']
age = [32, 31, 28, 28]

dict4 = {k:v for k, v in zip(name, age)}
dict4

dict5 = {k:v for k, v in zip(name, age) if v > 30}
dict5