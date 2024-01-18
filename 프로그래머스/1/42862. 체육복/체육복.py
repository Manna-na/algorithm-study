def solution(n, lost, reserve):
    reserve_r = [r for r in reserve if r not in lost]
    lost_r = [l for l in lost if l not in reserve]
    reserve_r.sort()
    lost_r.sort()
    for r in reserve_r:
        if r-1 in lost_r:
            lost_r.remove(r-1)
        elif r+1 in lost_r:
            lost_r.remove(r+1)
        
    return n - len(lost_r)