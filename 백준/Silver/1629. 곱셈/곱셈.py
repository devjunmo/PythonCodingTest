def power(a, b):
    if b == 1: # b의 값이 1이면 a % C를 return
        return a % C
    else:
        temp = power(a, b // 2) # a^(b // 2) 값을 미리 계산
        if b % 2 == 0:
            return temp * temp % C # b가 짝수인 경우
        else:
            return temp * temp * a % C # b가 홀수인 경우

A, B, C = map(int, input().split())
print(power(A, B))
