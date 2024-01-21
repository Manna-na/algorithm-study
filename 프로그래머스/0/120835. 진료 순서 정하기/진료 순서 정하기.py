def solution(emergency):
    result = []
    for e in range(len(emergency)):
        count = 1
        for ee in emergency:
            if emergency[e] != ee and emergency[e] > ee:
                count += 1
        result.append(len(emergency)-count+1)
                
    return result