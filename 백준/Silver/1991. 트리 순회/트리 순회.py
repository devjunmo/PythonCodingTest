from collections import defaultdict

tree = defaultdict(list)
N = int(input())

for i in range(N):
    root, left, right = list(input().split(" "))
    tree[root] = [left, right]

res = []


# 전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
def preorder(_root):
    if _root =='.':
        return
    
    res.append(_root)  # 먼저 방문
    l, r = tree[_root]
    preorder(l)
    preorder(r)
    
preorder('A')  # ABDCEFG
print("".join(res))
res = []  # 결과 버퍼 초기화


# 중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
def inorder(_root):
    if _root =='.':
        return
    
    # 왼, 오 검색
    l, r = tree[_root]
    inorder(l)  # 선 왼쪽
    res.append(_root)  # 방문
    inorder(r)  # 후 오른쪽
    
inorder('A')  # DBAECFG
print("".join(res))
res = []  # 결과 버퍼 초기화
    
    
    
# 후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)
def postorder(_root):
    if _root =='.':
        return
    
    # 왼, 오 검색
    l, r = tree[_root]
    postorder(l)  # 선 왼쪽
    postorder(r)  # 후 오른쪽
    res.append(_root)  # 방문
    
postorder('A')  # DBAECFG
print("".join(res))
    
    
    