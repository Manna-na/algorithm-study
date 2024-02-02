import re
import sys
input = sys.stdin.readline

expression = input().strip()
list_e = re.split('([-|+])', expression)
result = int(list_e[0])
idx = 1
while idx < len(list_e):
    if list_e[idx] == '-':
        idx += 1
        minus_sum = 0
        while idx < len(list_e) and list_e[idx] != "-":
            if list_e[idx] != "+":
                minus_sum += int(list_e[idx])
            idx += 1
        result -= minus_sum
    else:
        if list_e[idx] != "+":
            result += int(list_e[idx])
        idx += 1

print(result)