'''
N개의 정수 A[1],A[2], ...,A[N]이 있을 때
이 안에 X라는 정수가 존재하는지 알아내기
'''

# 입력1: 자연수 N
# 입력2: N개의 정수 A[1],...,A[N]
# 입력3: M
# 입력4: M개의 수들

# 출력1: M개으 줄에 답 출력. 존재 시 1, 존재하지 않을 시 0

'''
try1: 무지성 찾기 (완전탐색) => 시간초과

N = int(input())
list_n = list(map(int, input().split()))

M = int(input())
list_m = list(map(int, input().split()))

for i in range(0, len(list_n), 1):
    if list_m[i] in list_n:
        print("1")
    else:
        print("0")
'''

N = int(input())
list_n = list(map(int, input().split()))

M = int(input())
list_m = list(map(int, input().split()))
