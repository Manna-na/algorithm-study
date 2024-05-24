ans = 0
r, c = 1, 1
for i in range(9):
    ls = list(map(int, input().split()))
    for l in range(9):
        if ls[l] > ans:
            ans = ls[l]
            r, c = i+1, l+1


print(ans)
print(r, c)