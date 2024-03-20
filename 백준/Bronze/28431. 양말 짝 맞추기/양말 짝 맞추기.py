import sys
input = sys.stdin.readline

array = [int(input()) for _ in range(5)]
result = 0
hash = {i:0 for i in array}
for i in array:
    hash[i] += 1
for h in hash.items():
    if h[1] % 2 == 1:
        print(h[0])
        break