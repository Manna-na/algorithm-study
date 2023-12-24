import sys
input = sys.stdin.readline
n = int(input())
start = 666
count = 1
while count < n:
    start += 1
    if "666" in str(start):
        count += 1
print(start)