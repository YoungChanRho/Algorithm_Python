import sys
sys.stdin = open('sample_input.txt','r')

# 첫 줄에 노선 수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
# 각 노선별로 K, N, M이 주어지고, 다음줄에 M개의 정류장 번호가 주어진다. ( 1 ≤ K, N, M ≤ 100 )
# #과 노선번호, 빈칸에 이어 최소 충전횟수 또는 0을 출력한다.

T=int(input())      # 노선수
for test_case in range(1, T+1):
    K, N, M = map(int,input().split())
    arr = list(map(int,input().split()))
    # 주유소가 위치한 값들이 담긴 리스트가 생긴다.
    # ex. arr = [3, 5, 7, 9]
    # K = (한번에 이동할 수 있는 거리)
    # N = 도착지점
    arrive = [0]*(N+1)
    for i in arr:
        arrive[i] += 1    
    cnt = 0
    idx = 0
    cnt_end = 0
    while True:
        if idx+K >= N:
            break                           
        elif cnt_end == K:         
            cnt = 0
            break
        else:
            if arrive[idx+K] == 1:
                idx = idx + K
                cnt += 1
                cnt_end = 0
                continue
            elif arrive[idx+K] != 1:
                idx -= 1
                cnt_end +=1
                continue

    print('{} {}'.format(test_case, cnt))