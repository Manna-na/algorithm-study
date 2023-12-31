# dn 구하기
def d(n):
    return n + sum(map(int, str(n)))
# 셀프 넘버에 dn 값 추가
generated = set()
for i in range(1, 10000):
    generated.add(d(i))
answer = [i for i in range(1, 10000) if i not in generated]
for i in answer:
    print(i)