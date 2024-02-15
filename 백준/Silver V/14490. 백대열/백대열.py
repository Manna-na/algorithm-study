import sys
import math
input = sys.stdin.readline
nums = list(map(int, input().split(":")))
gcd = math.gcd(nums[0], nums[1])
print(f"{nums[0]//gcd}:{nums[1]//gcd}")