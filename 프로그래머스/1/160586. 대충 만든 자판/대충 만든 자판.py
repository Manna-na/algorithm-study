import sys


def solution(keymap, targets):
    answer = []
    for i in range(len(targets)):
        press = 0
        for j in targets[i]: 
            idx = 102
            for k in range(len(keymap)):
                now_idx = keymap[k].find(j)             
                if now_idx != -1 and idx > now_idx:
                    idx = now_idx
            if idx == 102:
                press = -1
                break
            press += idx + 1            
        answer.append(press)
                
    return answer