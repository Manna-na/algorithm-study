import sys
import math
input = sys.stdin.readline

while True:
    one, two, three = map(int, input().split())
    list = [one, two, three]
    list.sort()
    if one == two == three == 0:
        break
    if math.sqrt(list[0]**2+list[1]**2) == list[2]:
        print("right")
    else:
        print("wrong")