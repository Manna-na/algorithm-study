def solution(s):
    answer = 0
    englishes = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for english in range(len(englishes)):
        if englishes[english] in s:
            s = s.replace(englishes[english], str(english))
    s = int(s)
    return s