def solution(s, n):
    answer = ''
    for word in s:
        if word == " ":
            answer += " "
        elif ord(word) >= 65 and ord(word) <= 90:
            if ord(word) + n > 90:
                answer += chr(ord(word)+n-26)
            else:
                answer += chr(ord(word)+n)
        else:
            if ord(word) + n > 122:
                answer += chr(ord(word)+n-26)
            else:
                answer += chr(ord(word)+n)
    return answer