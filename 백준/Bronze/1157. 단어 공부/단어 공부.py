import sys
input = sys.stdin.readline

str = input().rstrip()
str = str.upper()
dict = {}
for i in str:
    dict[i] = dict.get(i, 0)+1

max_val = max(dict.values())
result = ''
isFlag = True
count = 0
for i, v in dict.items():
    if v == max_val:
        count += 1
        result = i
    if count > 1:
        print("?")
        isFlag = False
        break

if isFlag:
    print(result)