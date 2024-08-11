cnt = 0
while True:
    n = int(input())

    if n % 2 == 0:
        print(n//2)
        cnt += 1

        if cnt >= 3: # cnt 체크를 뒤에 해줘야 while문이 한번 더 돌지 않게 됨! (입력을 한 번 더 받게 되는 것을 방지)
            break