n = int(input())
votes = [int(input()) for _ in range(n)]

# 다솜이의 득표수
dasom_votes = votes[0]

# 다솜이를 제외한 후보들의 득표수
other_votes = sorted(votes[1:], reverse=True)

# 매수해야 하는 사람의 수
bribes = 0

while other_votes and other_votes[0] >= dasom_votes:
    # 가장 많은 득표수를 가진 후보의 득표수를 하나 줄임
    other_votes[0] -= 1
    # 다솜이의 득표수를 하나 증가
    dasom_votes += 1
    bribes += 1
    # 리스트를 다시 정렬
    other_votes.sort(reverse=True)

print(bribes)