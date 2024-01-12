import sys
input = sys.stdin.readline

c_array, m_array = [], []
for i in range(3):
    c,m = map(int, input().split())
    c_array.append(c)
    m_array.append(m)

for i in range(100):
    if m_array[i % 3]+m_array[(i+1)%3] > c_array[(i+1)%3]:
        temp = m_array[(i+1)%3]
        m_array[(i+1)%3] = c_array[(i+1)%3]
        m_array[i%3] =  m_array[i%3]+ temp - c_array[(i+1)%3]
    else:
        temp = m_array[i % 3]
        m_array[(i+1)%3] += temp
        m_array[i % 3] = 0
for m in m_array:
    print(m)