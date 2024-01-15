def solution(d, budget):
    d.sort()
    sum_arr = [d[0]]
    answer = 0
    for i in range(len(d)-1):
        sum_arr.append(sum_arr[i]+d[i+1])
    for i in range(len(sum_arr)):
        if sum_arr[i] > budget:
            answer = i
            break
        if sum_arr[i] == budget:
            answer = i+1
            break
        answer = len(d)
    return answer