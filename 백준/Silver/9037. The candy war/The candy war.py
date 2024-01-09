import sys
input = sys.stdin.readline

T = int(input())

# 사탕 짝수개 맞추기
def isEven(arr):
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            arr[i] += 1

# 사탕 순회
def circle(arr):
    temp = arr.copy()
    for i in range(len(arr)):
        arr[(i+1)%len(arr)] = temp[(i+1)%len(arr)] //2 + temp[i]//2
def total_candy(arr):
    isTrue = True
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            isTrue = False
    return isTrue
for _ in range(T):
    N = int(input()) # 아이의 인원
    C = list(map(int, input().split())) # 아이들이 초기에 가지고 있는 사탕의 수
    answer = 0 # 몇 번의 순환
    while True:
        isEven(C) # 먼저 짝수개 맞추기
        if total_candy(C): # 만약 모든 사탕의 수가 같다면 break
            break
        circle(C) # 사탕 순회하기
        answer += 1

    print(answer)