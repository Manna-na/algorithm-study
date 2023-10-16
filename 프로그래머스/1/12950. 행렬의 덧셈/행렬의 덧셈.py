def solution(arr1, arr2):
    answer = []
    for r in range(len(arr1)):
        answer1 = []    
        for c in range(len(arr1[r])):
            answer1.append(arr1[r][c] + arr2[r][c])
        answer.append(answer1)
 
    return answer