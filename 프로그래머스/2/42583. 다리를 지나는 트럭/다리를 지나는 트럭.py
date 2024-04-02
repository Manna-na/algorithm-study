from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)  # 다리를 0으로 초기화
    trucks = deque(truck_weights)
    current_weight = 0  # 현재 다리 위의 총 무게

    while trucks or current_weight:
        time += 1
        left_truck = bridge.popleft()  # 다리를 건넌 트럭
        current_weight -= left_truck
        if trucks:
            if current_weight + trucks[0] <= weight:  # 다리에 새로운 트럭이 진입할 수 있는 경우
                truck = trucks.popleft()
                bridge.append(truck)
                current_weight += truck
            else:  # 다리에 진입할 수 없는 경우
                bridge.append(0)
    return time
