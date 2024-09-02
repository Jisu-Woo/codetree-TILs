a = input()

max = 0
for i in range(len(a)):
    str = list(a)
    if str[i] == '0':
        str[i] = '1'
    else:
        str[i] = '0'
    
    str = ''.join(str)
    res = int(str, 2)
    if res > max:
        max = res

print(max)