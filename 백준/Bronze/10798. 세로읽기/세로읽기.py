import sys
input = sys.stdin.readline

words = []
for _ in range(5):
    words.append(input().rstrip())
max_length = max(len(word) for word in words)

# 세로로 읽은 결과를 저장할 변수
result = ""

# 가장 긴 단어의 길이만큼 반복
for i in range(max_length):
    # 각 단어를 순회
    for word in words:
        # 현재 인덱스에 해당하는 문자가 있는 경우 결과에 추가
        if i < len(word):
            result += word[i]

print(result)