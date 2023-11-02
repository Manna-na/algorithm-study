def solution(sizes):
    answer = 0
    arr_w = []
    arr_h = []
    for i in range(len(sizes)):
        if sizes[i][0] > sizes[i][1]:
            arr_w.append(sizes[i][0])
            arr_h.append(sizes[i][1])
        else:
            arr_w.append(sizes[i][1])
            arr_h.append(sizes[i][0])
    answer = max(arr_w) * max(arr_h)
    return answer