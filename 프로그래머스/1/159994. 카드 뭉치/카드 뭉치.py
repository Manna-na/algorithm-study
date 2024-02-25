from collections import deque

def solution(cards1, cards2, goal):
    q_c1, q_c2, q_g = deque(cards1), deque(cards2), deque(goal)
    for g in goal:
        if len(q_c1) > 0 and len(q_c2) > 0:
            c1, c2 = q_c1[0], q_c2[0]
            if g == c1:
                q_c1.popleft()
                q_g.popleft()
            elif g == c2:
                q_c2.popleft()
                q_g.popleft()
        elif len(q_c1) < 1:
            c2 = q_c2[0]
            if g == c2:
                q_c2.popleft()
                q_g.popleft()
        elif len(q_c2) < 1:
            c1 = q_c1[0]
            if g == c1:
                q_c1.popleft()
                q_g.popleft()
    if len(q_g) == 0:
        return "Yes"
    else:
        return "No"
            