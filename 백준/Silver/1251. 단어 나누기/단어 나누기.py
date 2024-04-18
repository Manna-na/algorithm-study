import sys
input = sys.stdin.readline

# 1. 두 부분을 골라서 쪼갠다고 했으니까, 이거는 구간을 먼저 잘 정하는게 중요하겠지
# 2. 각 구간에 해당하는 단어들 뒤집어
# 3. 합챠
# 4. 사전순 비교해봐
string = input().strip()
ans = string[::-1]
for i in range(1, len(string)):
    for j in range(i+1, len(string)):
        now_words = string[i-1::-1]+string[j-1:i-1:-1]+string[len(string)-1:j-1:-1]
        if now_words < ans:
            ans = now_words

print(ans)