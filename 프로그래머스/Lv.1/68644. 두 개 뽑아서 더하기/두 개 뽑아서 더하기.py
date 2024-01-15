def solution(numbers):
    answer = []
    test = []
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            test.append(numbers[i] + numbers[j])  
    test.sort()
    for val in test:
        if val not in answer:
            answer.append(val)
    return answer