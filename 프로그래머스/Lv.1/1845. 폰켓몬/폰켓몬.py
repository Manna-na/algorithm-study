def solution(nums):
    answer = 0
    poketmon = {}
    for num in nums:
        if poketmon.get(num):
            poketmon[num] += 1
        else:
            poketmon[num] = 1
    answer = min(len(poketmon), len(nums)//2)
        
    return answer