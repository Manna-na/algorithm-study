import sys
input = sys.stdin.readline
while True:
    sentance = list(input().rstrip('\n'))
    if not sentance:
        break
    numbers=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    small, large, number, blink = 0, 0, 0, 0
    for i in sentance:
        if i in numbers:
            number += 1
        if i == " ":
            blink += 1
        elif 65 <= ord(i) <= 90:
            large += 1
        elif 97 <= ord(i) <= 122:
            small += 1

    print(str(small), str(large), str(number), str(blink))
