import sys
input = sys.stdin.readline

# 시간복잡도 : 10^5 -> O(N) or O(nlogn)
# 1. 포인터 움직여
# 1-1. end index에 해당하는 값이 k개 미만이야? end index 하나 올려
# 1-2. end index에 해당하는 값이 k개 이상이야? now_length구하고 max 갱신, start index 하나올려
# 1-2-1. start index에 해당하는 값 하나 줄여 그래도 end index에 해당하는 값이 k개 초과면 또올려
# 1-2-2. start index에 해당하는 값 하나 줄이니까 k개 이하야? start index +1 한 상태로 다시 1-1 반복
n, k = map(int, input().split())
dohyeon = list(map(int, input().split()))
duplicate_dict = {}
start, end = 0, 0
max_length = 0
while end < n:
    if dohyeon[end] in duplicate_dict:
        if duplicate_dict[dohyeon[end]] <= k:
            duplicate_dict[dohyeon[end]] += 1
            end += 1
        else:
            max_length = max(max_length, end-start)
            duplicate_dict[dohyeon[start]] -= 1
            start += 1
    else:
        duplicate_dict[dohyeon[end]] = 1
    # print("start : ", start, "end : ", end)
    # print("max_length", max_length, "duplicate_dict : ", duplicate_dict)
if max_length < end-start:
    print(end-start)
else:
    print(max_length)