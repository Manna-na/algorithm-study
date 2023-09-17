n = int(input())
arr = list(map(int, input().split()))
sum = 0
for i in range(n):
    for j in range(i):
        if arr[j] > arr[i]:
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp

for i in range(n):
    cnt = 0
    for j in range(i+1):
        cnt += arr[j]
    sum += cnt

print(sum)
