def solution(k, score):
    answer, hall = [], []
    
    for i in range(len(score)):
        if i < k:
            hall = score[:i+1]
        else:
            if score[i] >= hall[-1]:
                hall[k-1] = score[i]
        hall.sort(reverse=True)
        answer.append(hall[-1]) 
    
        
    return answer
        
    
