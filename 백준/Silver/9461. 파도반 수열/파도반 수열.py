t = int(input())
arr = [ 0 for _ in range(101)]
arr[0] = arr[1] = arr[2] = 1
for i in range(3, 101):
    arr[i] = arr[i-3] + arr[i-2]

for i in range(t):
    n = int(input())
    print(arr[n-1])