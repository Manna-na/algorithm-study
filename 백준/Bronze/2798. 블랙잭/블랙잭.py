import sys

input = sys.stdin.readline

n, m = map(int, input().split())
array = list(map(int, input().split()))
array.sort(reverse=True)
isFlag = False
answer = 0
for i in range(n):
    one = array[i]
    for j in range(i+1, n):
       two = array[j]
       for k in range(j+1, n):
           three = array[k]
           if one+two+three <= m:
               if answer < one+two+three:
                   answer = one + two+ three
print(answer)