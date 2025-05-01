def solution(numbers):
    answer = []
    sum_list=[]
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            sum_list.append(numbers[i]+numbers[j])
    answer = list(set(sum_list))
    answer.sort()
    return answer