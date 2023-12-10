import sys
input = sys.stdin.readline

result = 0
arr = set()
for _ in range(int(input())):
    nickname = input().strip()
    if nickname == 'ENTER':
        arr.clear()
        continue
    if nickname not in arr:
        arr.add(nickname)
        result += 1
print(result)

