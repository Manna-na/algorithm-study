def solution(survey, choices):
    answer = ''
    disagree_score = {1:3, 2:2, 3:1, 4:0}
    agree_score = {5:1, 6:2, 7:3}
    types = {'R':0, 'C':0, 'J':0, 'A':0, 'T':0, 'F':0, 'M':0, 'N':0}
    for c in range(len(choices)):
        if choices[c] in disagree_score:
            types[survey[c][0]] += disagree_score[choices[c]]
        else:
            types[survey[c][1]] += agree_score[choices[c]]
            
    if types['R'] >= types['T']:
        answer += 'R'
    else:
        answer += 'T'
    if types['C'] >= types['F']:
        answer += 'C'
    else:
        answer += 'F'
    if types['J'] >= types['M']:
        answer += 'J'
    else:
        answer += 'M'
    if types['A']>= types['N']:
        answer += 'A'
    else:
        answer += 'N'
    return answer