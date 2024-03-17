import sys
input = sys.stdin.readline

# 시간복잡도 :O(N)
# 1. 제일 큰 값 찾아
# 2. 나머지들 /2 하고 더해

n = int(input())
array = list(map(int, input().split()))
# result = 0
max_energy = max(array)
result = max_energy
for i in array:
    if i == max_energy:
        continue
    result += i/2
print(result)