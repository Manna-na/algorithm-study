def solution(X, Y):
    array = []
    for i in range(9, -1, -1):
        count_val = min(X.count(str(i)), Y.count(str(i)))
        for _ in range(count_val):
            array.append(str(i))

    if len(array) == 0:
        return "-1"
    else:
        array.sort(reverse=True)
        if array[0] == "0":
            return "0"         
        else:   
            return "".join(array)

