def solution(s):
    englishes = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for english in range(len(englishes)):
        if englishes[english] in s:
            s = s.replace(englishes[english], str(english))
    s = int(s)
    return s

# def solution(s):
#     words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

#     for i in range(len(words)):
#         s = s.replace(words[i], str(i))

#     return int(s)