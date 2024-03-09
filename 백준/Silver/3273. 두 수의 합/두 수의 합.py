import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
x = int(input())
result = 0
array.sort()
start, end = 0, len(array)-1

while start < end:
    curr_sum = array[start] + array[end]

    if curr_sum == x:
        result += 1
        start += 1
        end -= 1
    elif curr_sum < x:
        start += 1
    else:
        end -= 1

print(result)