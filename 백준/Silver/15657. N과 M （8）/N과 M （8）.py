def generate_sequences(arr, M):
    arr.sort()
    result = []

    def backtrack(start, path):
        if len(path) == M:
            result.append(path[:])
            return

        prev = -1
        for i in range(start, len(arr)):
            if arr[i] == prev:  # 같은 수는 스킵하여 중복 제거
                continue
            path.append(arr[i])
            backtrack(i, path)  # i 부터 시작하여 중복 선택 허용
            path.pop()
            prev = arr[i]

    backtrack(0, [])
    return result


# 입력 처리
N, M = map(int, input().split())
arr = list(map(int, input().split()))

# 함수 호출 및 결과 출력
sequences = generate_sequences(arr, M)
for sequence in sequences:
    print(' '.join(map(str, sequence)))