import sys
input = sys.stdin.readline
list_str = list(input())
list_alphabet = [chr(i) for i in range(97, 123)]
for alphabet in list_alphabet:
    if alphabet in list_str:
        print(list_str.index(alphabet), end=" ")
    else:
        print(-1, end=" ")