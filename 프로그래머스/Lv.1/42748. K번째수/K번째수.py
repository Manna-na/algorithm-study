def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        list = []
        for j in range(commands[i][0]-1, commands[i][1]):
            list.append(array[j])
        list.sort()
        answer.append(list[commands[i][2]-1])
    return answer