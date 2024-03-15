def solution(id_list, report, k):

    # 1. id 별 신고한 uid, id별 신고받은 횟수 저장
    report_dict = {i:[] for i in id_list}
    report_count_dict = {i:0 for i in id_list}
    for i in range(len(report)):
        reporter, reported_people = report[i].split(" ")
        if reported_people not in report_dict[reporter]:      
            report_dict[reporter].append(reported_people)
            report_count_dict[reported_people] += 1

    answer = [0 for _ in range(len(id_list))]
        
    # 2. 신고받은 횟수가 k 이상인 경우 신고자 id 탐색
    for i, v in report_count_dict.items():
        print(i, v)
        if v >= k:
            for d_i, d_v in report_dict.items():
                
                if i in d_v:
                    reporter_idx = id_list.index(d_i)
                    # 3. 배열로 저장
                    answer[reporter_idx] += 1
        

    return answer