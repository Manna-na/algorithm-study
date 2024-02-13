def solution(bandage, health, attacks):
    power = health
    attack_idx = 0
    bandage_count = 0
    for i in range(attacks[-1][0]+1):
        if attacks[attack_idx][0] != i: # 공격 아닐 때
            bandage_count += 1
            if bandage_count < bandage[0]: # 시전 시간 이전
                if power + bandage[1] < health:
                    power += bandage[1]
                else:
                    power = health
            else: # 시전 시간
                if power + bandage[1] + bandage[2] < health:
                    power += bandage[1] + bandage[2]
                else:
                    power = health
                bandage_count = 0
        else: # 공격일 때
            power -= attacks[attack_idx][1]
            bandage_count = 0
            if power <= 0:
                return -1
            if attack_idx + 1 == len(attacks):
                return power
            attack_idx += 1

                
                