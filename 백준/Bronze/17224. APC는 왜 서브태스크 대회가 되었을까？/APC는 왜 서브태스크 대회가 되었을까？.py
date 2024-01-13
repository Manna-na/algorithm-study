import sys
input = sys.stdin.readline

N, L, K = map(int, input().split())
sub_arr = []
for i in range(N):
    sub_arr.append(list(map(int, input().split())))

sub_arr.sort(key=lambda x:(x[1],x[0]))

answer = 0
for i in range(N):
    max_val, min_val = sub_arr[i][1], sub_arr[i][0]
    if K > 0:
        if max_val <= L:
            answer += 140
            K-=1
        else:
            if min_val <= L:
                answer += 100
                K-=1
    else:
        break
print(answer)