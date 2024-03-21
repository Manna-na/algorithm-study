# 10^6 -> 시간복잡도:O(nlogn)
# 문자열을 어떻게 처리할 것 인가
def solution(s):
    s = s[2:-2].split('},{')
    sorted_s = sorted(s, key=lambda x:len(x))
    answer = []
    for ss in sorted_s:
        list_ss = ss.split(',')
        for sss in list_ss:
            if int(sss) not in answer:
                answer.append(int(sss))
    return answer