'''
두 마리의 백조가 호수에 살고있다
호수는 행이 R개, 열이 C개인 직사각형
호수의 어떤 칸은 얼음으로 덮여있음
호수는 차례로 녹는데, 매일 물 공간과 접촉한 모든 빙판 공간은 녹음
두 공간이 접촉하려면 가로나 세로로 닿아있는 것만 고려

백조는 물 공간에서 세로나 가로로만 이동 가능
며칠이 지나야 백조들이 만날 수 있는지 계산하는 프로그램
'''

# 입력1: 첫째 줄에 R과 C
# 입력2: R개의 줄에는 각각 길이 C의 문자열(.은 물, X는 빙판, L은 백조)

# 출력1: 첫째 줄에서 문제에서 주어진 걸리는 날 출력

import sys
import collections
R, C = map(int, sys.stdin.readline().split(" "))

lake = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]

swans = []
waters = []
visited = [[0 for i in range(C)] for i in range(R)]

# 입력
for i in range(R):
    line = input()

    for j in range(C):
        if line[j] == 'L':
            swans.append((i, j))
            waters.append((i,j))

        if line[j] == '.':
            waters.append((i,j))
    lake.append(list(line))

def melt_ice():
    new_water= []
    global waters
    
    for water in waters:
        y, x = water
        for i in range(4):
            t_y, t_x = y + dy[i], x + dx[i]

            if t_y < R and t_x < C and t_y >= 0 and t_x >= 0:
                if lake[t_y][t_x] == 'X':
                    lake[t_y][t_x] = '.'
                    new_water.append((t_y,t_x))
    waters = new_water

def check(q):
    next_q = collections.deque()
    while q:
        y, x = q.popleft()
        visited[y][x] = 1

        for i in range(4):
            n_y, n_x = y+dy[i], x+dx[i]
            if n_y < 0 or n_y >= R or n_x < 0 or n_x >= C: continue
            if(visited[n_y][n_x] == 1):  continue

            visited[n_y][n_x] = 1
            if lake[n_y][n_x] == 'L':
                return True, next_q

            if lake[n_y][n_x] == '.':
                q.append((n_y, n_x))
    
            if lake[n_y][n_x] == 'X': 
                next_q.append((n_y, n_x))
    return False, next_q

q = collections.deque()
q.append(swans[0])

count = 0

while True:
    success, q = check(q)

    if success:
        break
    count += 1
    melt_ice()

#     print("lake")
#     for i in range(R):
#         for j in range(C):
#             print(lake[i][j], end='')
#         print()

print(count)