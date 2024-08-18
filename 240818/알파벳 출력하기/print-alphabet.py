n = int(input())

cnt = ord('A')
for i in range(n):
    for j in range(i + 1):
        if cnt > ord('Z'): # Z 다음은 A로 초기화
            cnt = ord('A')
        print(chr(cnt), end="")
        cnt += 1
    print()