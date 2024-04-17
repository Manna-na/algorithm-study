import sys
import math
input = sys.stdin.readline

a, b = map(int, input().split())
minus_val = (-2*a-math.sqrt((2*a)**2-4*b))//2
plus_val = (-2*a+math.sqrt((2*a)**2-4*b))//2
if plus_val == minus_val:
    print(int(plus_val))
else:
    print(int(minus_val), int(plus_val))