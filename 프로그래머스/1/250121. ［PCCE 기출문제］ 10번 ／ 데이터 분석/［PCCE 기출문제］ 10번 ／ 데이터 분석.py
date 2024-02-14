def solution(data, ext, val_ext, sort_by):
    answer = []
    columns = ["code", "date", "maximum", "remain"]
    sorted_data = sorted(data, key=lambda x :x[columns.index(sort_by)])
    for data in sorted_data:
        if data[columns.index(ext)] < val_ext:
            answer.append(data)
    return answer