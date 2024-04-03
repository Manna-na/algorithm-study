import sys
input = sys.stdin.readline

# dict = {'ABC':2, 'DEF':3, 'GHI':4, 'JKL':5, 'MNO':6, 'PQRS':7, 'TUV':8, 'WXYZ':9 }
# str = input()
# print(str)
# for i, v in dict.items():
#     for s in str:
#         if s in i:
#             print(i)

dial_dict = {
    'ABC': 2, 'DEF': 3, 'GHI': 4, 'JKL': 5,
    'MNO': 6, 'PQRS': 7, 'TUV': 8, 'WXYZ': 9
}
word = input()
# 시간 계산
time = 0
for letter in word:
    for key in dial_dict.keys():
        if letter in key:
            # 숫자 1을 걸 때 2초가 필요하므로, 2초를 더해준다.
            time += dial_dict[key] + 1
            break
print(time)