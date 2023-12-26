def solution(participant, completion):
    answer = ''
    humans = {}
    for p in participant:
        if humans.get(p):
            humans[p] += 1
        else:
            humans[p] = 1
    
    for c in completion:
        humans[c] -= 1
    
    for key, value in humans.items():
        if value > 0:
            answer+=key
    
        
            
    return answer