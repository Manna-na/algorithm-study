import sys
input = sys.stdin.readline

str = input()
res = 1
for i in range(len(str)//2):
    if str[i] != str[len(str)-2-i]: #0 1
        res = 0
print(res)