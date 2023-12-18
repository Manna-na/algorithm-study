import sys
input = sys.stdin.readline

cro_words = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
cro_input = input().strip()
count = 0
num = 0
while num < len(cro_input):
    if num + 2 < len(cro_input) and cro_input[num:num+3] in cro_words:
        count += 1
        num += 3
    elif num + 1 < len(cro_input) and cro_input[num:num+2] in cro_words:
        count += 1
        num += 2
    else:
        count += 1
        num += 1
print(count)
