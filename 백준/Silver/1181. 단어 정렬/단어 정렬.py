n = int(input())
word_list = [input() for _ in range(n)]
word_list = list(set(word_list))
word_list.sort()
sort_list = sorted(word_list, key=lambda x: len(x))
for word in sort_list:
    print(word, end='\n')
