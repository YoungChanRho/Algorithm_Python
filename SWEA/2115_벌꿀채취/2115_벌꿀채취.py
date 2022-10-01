import sys
import time
sys.stdin = open('input.txt','r')

T = int(input())

for tc in range(1,T+1):
    N, M, C = map(int,input().split())    # N: 배열 크기, M: 선택할 수 있는 벌통 개수, C: 최대 양
    arr = [list(map(int,input() .split())) for _ in range(N)]

    result = []    # 합의 정보를 담을 리스트
    for i in range(N):
        for j in range(0,N-M+1):
            # 먼저 합을 
            summ = 0
            if sum(arr[i][j:j+M]) <= C:    # 최대 양보다 작다면
                for k in range(M):
                    summ += arr[i][j+k]**2    # 제곱한 합을 더해준다.
                result.append((i,j,summ))    # 튜플로 담아준다.
            else:    # 범위 내에 없을 경우
                for k in range(1, 1<<M):
                    # 부분집합을 구해준다.
                    subset = []
                    # 부분집합을 구할때마다 초기화 시켜준다.
                    sum2 = 0    # sum값도 초기화
                    for l in range(M):
                        if k & (1<<l):
                            subset.append(arr[i][j+l])
                    if sum(subset) <= C:
                        for m in range(len(subset)):
                            sum2 += subset[m]**2
                            result.append((i,j,sum2))
    sorted_result = sorted(result, key = lambda x : x[2], reverse=True)
    ans_1 = sorted_result[0][2]

    # 만약 최댓값과 두번째 최댓값의 범위가 겹친다면
    # 두번쨰 최대값의 시작 위치 <= 첫번째 값의 마지막 위치
    # 두번째 최대값의 끝나는 위치 >= 첫번째 값의 시작 위치
    if sorted_result[0][0] == sorted_result[1][0] and (sorted_result[1][1] <= sorted_result[0][1]+M-1 or sorted_result[1][1]+M-1>=sorted_result[0][1]):
        # 그 다음 값부터 탐색을 시작하는데
        for i in range(2,len(sorted_result)):
            if sorted_result[0][0] != sorted_result[i][0]:
                print("#{} {}".format(tc,ans_1 + sorted_result[i][2]))
                break
    else:
        print("#{} {}".format(tc,sorted_result[0][2] + sorted_result[1][2]))
    