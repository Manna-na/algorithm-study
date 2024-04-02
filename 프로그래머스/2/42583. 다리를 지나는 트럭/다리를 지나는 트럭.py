from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = deque([])
    truck_weights_q = deque(truck_weights)
    time = 0 # 내가 확인하려는 경과 시간
    while truck_weights_q:
        queue.append(truck_weights_q.popleft())
        time += bridge_length
        while truck_weights_q:
            if len(queue) <= bridge_length and sum(queue) + truck_weights_q[0] <= weight:
                queue.append(truck_weights_q.popleft())
                time += 1
            else:
                break

    return time