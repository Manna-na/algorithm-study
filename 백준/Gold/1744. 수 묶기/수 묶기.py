import sys
from queue import PriorityQueue

input = sys.stdin.readline
plusPque = PriorityQueue()
minusPque = PriorityQueue()
N = int(input())
for _ in range(N):
    data = int(input())
    if data > 0 :
        plusPque.put(data*-1) # 양수 내림차순 정렬 위해 -1 곱해서 저장
    else:
        minusPque.put(data)

result = 0


# 음수 처리
while minusPque.qsize() > 0:
    num1 = minusPque.get()
    if num1 == 0:
        continue
    if minusPque.qsize() >= 1:
        num2 = minusPque.get()
        if num2 <= 0:
            result += num1 * num2
            # print(f"{num1} {num2}일때 -> {result}")
    else:
        result += num1

# 양수 처리
while plusPque.qsize() > 0:
    num1 = plusPque.get()
    if num1 == -1:
        result += num1*-1
    else:
        if plusPque.qsize() >= 1:
            num2 = plusPque.get()
            if num2 == -1:
                # print(1+num1*-1)
                result += 1 + (num1*-1)
            else:
                result += num1 * num2
                # print(f"{num1 * -1} {num2 * -1}일때 -> {result}")
        else:
            result += num1 * -1

print(result)