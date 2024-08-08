a = input().split()
b = input().split()
c = input().split()
cnt = 0

if a[0] == 'Y' and int(a[1]) >= 37:
    cnt += 1
if b[0] == 'Y' and int(b[1]) >= 37:
    cnt += 1
if c[0] == 'Y' and int(c[1]) >= 37:
    cnt += 1


if cnt >= 2:
    print('E')
else:
    print('N')