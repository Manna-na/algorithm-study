n = int(input())
isTrue=False
for i in range(1, 1000001):
    num = i
    answer = i
    while num > 0:
        answer += num % 10
        num //= 10
    if answer == n:
        isTrue = True
        print(i)
        break

if not isTrue:
    print(0)