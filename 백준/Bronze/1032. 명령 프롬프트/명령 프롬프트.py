import sys
input = sys.stdin.readline

n = int(input())
word = input().strip()
if n > 1:
    for _ in range(n-1):
        now_word = input().strip()
        answer = ''
        for w, nw in zip(word, now_word):
            if w == nw:
                answer += w
            else:
                answer += '?'
        word = answer


print(word)