str = map(str, input())
arr = [chr(i) for i in range(97, 123)]
answer = [-1 for _ in range(26)]
for index, num in enumerate(str):
    if num in arr:
        index_num = arr.index(num)
        if answer[index_num] == -1:
            answer[index_num] = index

print(*answer)