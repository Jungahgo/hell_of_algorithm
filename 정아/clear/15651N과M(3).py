'''
N과 M이 주어졌을 때
- 1부터 N까지 자연수 중 M개를 고른 수열
- 같은 수를 여러 번 골라도 됨
을 만족하는 길이가 M인 수열을 모두 구하기
'''

# 입력1: N,M

# 출력1: 한 줄에 하나씩 문제의 조건을 만족하는 수열 출력
#        중복 수열은 출력하지 않는다

N,M = map(int, input().split())

l = [0] * M

def print_list(l):
    for i in range(0, M, 1):
        print(l[i],end = " ")
    print()

def dfs(l, loc):
    if (loc == M):
        print_list(l)
        return
    for i in range(1, N+1, 1):
        l[loc] = i
        dfs(l, loc+1)

dfs(l,0)