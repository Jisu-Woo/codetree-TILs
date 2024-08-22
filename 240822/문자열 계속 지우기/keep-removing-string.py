str1 = input()
str2 = input()


while True:
    if str1.find(str2) == -1:  # 없으면 끝
        break
    else:
        idx = str1.find(str2)
        str1 = str1[0:idx] + str1[idx + len(str2):]


print(str1)