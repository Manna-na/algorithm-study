n = input()
word_list = [input() for _ in range(int(n))]
result = 0
for word in word_list:
    last_seen={}
    isGroup = True
    for i, char in enumerate(word):
        # last_seen에 현재 값이 존재하고, 그 위치가 현재 위치 직전이 아니라면 break
       if char in last_seen and i-last_seen[char] != 1:
           isGroup = False
           break
       last_seen[char] = i
    if isGroup:
        result += 1
print(result)
