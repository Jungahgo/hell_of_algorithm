'''
N개의 물건
무게: W, 가치: V
무게 K만큼 넣을 수 있을 때 가치의 최댓값 
'''

# 입력1: 물품의 수 N, 무게 K
# 입력2: N개의 줄에 거쳐 각 물건의 무게 W, 물건의 가치 V

# 출력1: 물건들의 가치의 최댓값

N,K = map(int, input().split())
list_w = [0] * N
list_v = [0] * N

for i in range(0,N,1):
    W,V = map(int, input().split())
    list_w[i] = W
    list_v[i] = V 

# DP

