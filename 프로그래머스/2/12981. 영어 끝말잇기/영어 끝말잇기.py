def solution(n, words):
    answer = [0, 0]
    stack_w = [words[0]]
    words_lenght = len(words)
    for i in range(1, words_lenght):
        if stack_w[i-1][-1] == words[i][0]:
            if words[i] in stack_w:
                answer[0] = i % n + 1
                answer[1] = i // n + 1
                break
            stack_w.append(words[i])
        else:
            answer[0] = i % n + 1
            answer[1] = i // n + 1
            break
    return answer
