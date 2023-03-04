from base64 import b64decode

T = int(input())
for t in range(1, T+1):
    print(f'#{t} {b64decode(input()).decode("UTF-8")}')
