'''
자연수 N과 M
조건을 만족하는 길이가 M인 수열 구하기
- 1부터 N까지 자연수 중 M개를 고른 수열
- 같은 수를 여러 번 골라도 ㄱㅊ
- 고른 수열은 비내림차순이어야함
'''

N,M = map(int, input().split())

l = [0]*M

def print_list(l):
    for i in range(0, M, 1):
        print(l[i],end = " ")
    print()

def dfs(l, loc, start):
    if (loc == M):
        print_list(l)
        return

    for i in range(start, N+1, 1):
        l[loc] = i
        dfs(l, loc+1, i)

dfs(l, 0, 1)