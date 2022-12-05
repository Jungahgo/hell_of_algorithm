'''
0부터 n까지의 정수 k개를 더하여 
합이 n이 되는 경우의 수를 구하는 프로그램
덧셈의 순서가 바뀐경우는 다른 경우로 셈, 하나의 수 여러 번 사용가능
'''

# 입력1: n, k

# 출력1: 답을 1,000,000,000으로 나눈 나머지

'''
1. 완전탐색 
-> 시간초과로 실패

n, k = map(int, input().split())

l = [0] * k
answer = 0

def dfs(l, loc):
    global answer 

    if (loc == k):
        if (sum(l) == n): 
            answer += 1
        return
    
    for i in range(0, n + 1, 1):
        l[loc] = i
        dfs(l, loc + 1)

dfs(l, 0)
print(answer % 1000000000)

'''
