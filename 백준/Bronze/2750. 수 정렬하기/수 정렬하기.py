n = int(input())
l = []
for _ in range(n):
    l.append(int(input()))

for i in range(n-1):
    for j in range(n-1-i):
        if l[j] > l[j+1]:
            temp = l[j]
            l[j] = l[j + 1]
            l[j+1] = temp


for i in range(n):
    print(l[i])