import sys
input = sys.stdin.readline
# 시간복잡도 : 10^5 -> O(nlogn), 이분탐색
n, m = map(int, input().split())
array = list(map(int, input().split()))
# ?? 이거 어떻게 m으로 나눠?
# 나누는걸 먼저 생각하는게 아니야, 상한과 하한을 어떻게 할지를 먼저 생각해 이진탐색이잖니
# 하한 : 동영상 가장 긴 시간
# 상한 : 동영상 총합
# m개의 블루레이에 강의를 나누어 담을 수 있는지
# m개의 블루레이로 담지 못하면 블루레이 크기를 늘린다.
start, end = max(array), sum(array)
while start <= end:
    mid = (start + end) // 2
    now_sum, count = 0, 0
    for r in array:
        curr = now_sum + r
        if curr <= mid:
            now_sum += r
        else:
            count += 1
            now_sum = r
    # print("start : ", start, "end : ", end, "mid :", mid, "now_sum:", now_sum, "count : ", count)
    # 마지막에 남은 강의들을 위한 블루레이 추가
    if now_sum:
        count += 1
    if count > m:
        start = mid + 1
    elif count <= m:
        end = mid -1

print(start)