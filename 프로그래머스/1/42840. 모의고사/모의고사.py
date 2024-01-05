def solution(answers):
    peoples = {1:[1, 2, 3, 4, 5], 2:[2, 1, 2, 3, 2, 4, 2, 5], 3: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]}
    dict = {1:0, 2:0, 3:0}
    for j in range(1, 4):
        for k in range(len(answers)):
            ans = peoples[j][k % len(peoples[j])]
            print(answers[k], ans)
            if ans == answers[k]:
                dict[j] += 1
    sorted_dict = sorted(dict.items(), key=lambda x:x[1], reverse = True)
    max_val = sorted_dict[0][1]
    answer = []
    for i in sorted_dict:
        if max_val == i[1]:         
            answer.append(i[0])
    
    return answer