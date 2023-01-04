'''
앱
실행 중인 앱은 하나지만, 많은 앱들이 활성화되어있음
-> 메모리 부족 상태가 오게 됨
=> 앱 비활성화 필요

N개의 앱, A1-AN이 활성화되어있다고 할 때,
Ai는 Mi바이트 만큼의 메모리를 사용
Ai를 비활성화 한 후 다시 실행 시 추가적으로 들어가는 비용이 Ci

사용자가 새로운 앱 B를 실행하고자하여, 추가로 M 바이트의 메모리가 필요할 때
(활성화되어있는 앱 중 몇 개를 비활성화하여 M바이트 이상의 메모리 추가로 확보)

비활성화 했을 경우의 비용 Ci의 합을 최소화하여 필요한 메모리 M바이트를 확보하는 방법을 찾아야함
'''

# 입력1: N, M
# 입력2: N개의 현재 활성화 되어있는 앱이 사용중인 메모리 바이트
# 입력3: N개의 각 앱을 비활성화 했을 경우의 비용

# 출력1: 필요한 메모리 M을 확보하기 위한 앱 비활성화의 최소 비용

N, M = map(int, input().split())
Mlist = list(map(int,input().split()))
Clist = list(map(int,input().split()))

#DP

Csum = sum(Clist)
dp = [[0 for i in range(Csum+1)] for j in range(N+1)]
for i in range(1,N+1):
    for j in range(Csum+1):
        if (Clist[i-1] - j <= 0):
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-Clist[i-1]] + Mlist[i-1])
        else:
            dp[i][j] = dp[i-1][j]

for i in range(Csum+1):
    if dp[N][i] >= M:
        print(i)
        break
        