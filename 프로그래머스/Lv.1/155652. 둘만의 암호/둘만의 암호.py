def solution(s, skip, index):
    alphabet = [chr(i) for i in range(97, 123) if chr(i) not in skip]

    answer = ''
    for char in s:
        char_index = alphabet.index(char)
        shifted_char = alphabet[(char_index + index) % len(alphabet)]
        answer += shifted_char

    return answer