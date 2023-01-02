'''
치즈
한 시간마다 공기와 접촉된 부분 녹는다
치즈가 모두 녹아 없어지는 데 걸리는 시간과
모두 녹기 한 시간 전 남아있는 치즈조각이 놓여있는 칸의 개수
'''

# 입력1: 사각형 모양 판의 세로와 가로의 길이 (최대 100)
# 입력2: 치즈판 (치즈없:0, 치즈있:1) (숫자사이 빈칸있음)

# 출력1: 치즈가 모두 녹아 없어지는 데 걸리는 시간
# 출력2: 모두 녹기 한 시간 전 남아있는 치즈조각


from collections import deque

a,b = map(int,input().split())
l = []
q = deque()
v = [[0 for i in range(b)] for i in range(a)]
x = [0,1,0,-1]
y = [1,0,-1,0]

for i in range(a):
    temp = list(map(int, input().split(' ')))
    l.append(temp)

for i in range(a):
    for j in range(b):
        if (l[i][j] == 0):
            q.append([i,j])
            v[i][j] = 1

while (q):
    temp = q.popleft()
    for i in range(4):
        if (0 <= temp[0]+x[i] < a and 0 <= temp[1]+y[i] < b):
            if (l[temp[0]+x[i]][temp[1]+y[i]] == 1 
                and v[temp[0]+x[i]][temp[1]+y[i]] == 0):
                l[temp[0]+x[i]][temp[1]+y[i]] = 0
                v[temp[0]+x[i]][temp[1]+y[i]] = v[temp[0]][temp[1]]+1
                q.append([temp[0]+x[i], temp[1]+y[i]])
