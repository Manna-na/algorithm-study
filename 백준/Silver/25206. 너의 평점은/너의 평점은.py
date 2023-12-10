arr = [input().split() for _ in range(20)]

grade = {}
for i in range(20):
    if arr[i][2] == 'P':
        continue
    if arr[i][2] in grade:
        grade[arr[i][2]].append(float(arr[i][1]))
    else:
        grade[arr[i][2]] = [float(arr[i][1])]

grade_dict = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0': 2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}
result = 0
sum_grade = 0
for i in grade.keys():
    sum_grade += sum(grade.get(i))
    result += grade_dict.get(i) * sum(grade.get(i))
print(result/sum_grade)
