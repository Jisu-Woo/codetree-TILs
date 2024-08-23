str = input()

char = str[0]
cnt = 1

out_str = ""
for i in range(1, len(str)):
    if str[i] == str[i - 1]:
        cnt += 1
    else:
        out_str += char
        out_str += f"{cnt}"

        char = str[i]
        cnt = 1

out_str += char
out_str += f"{cnt}"

print(len(out_str))
print(out_str)