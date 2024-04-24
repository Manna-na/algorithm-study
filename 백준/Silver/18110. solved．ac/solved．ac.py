import sys
input = sys.stdin.readline

# 시간복잡도 : 10^5-> O(nlogn)안에 끝내야해

n = int(input())
levels = [int(input()) for _ in range(n)]
levels.sort()

def roundUp(num):
    if int(num) == 0:
        if num < 0.5:
            return 0
        else:
            return 1
    elif num % int(num) < 0.5:
        return int(num)
    else:
        return int(num) + 1

except_peoples = roundUp(n*0.15)
if n > 0:print(roundUp(sum(levels[except_peoples:n-except_peoples])/(n-except_peoples*2)))
else: print(0)