import sys
sys.stdin = open('algo2_sample_in.txt','r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())    # 줄 갯수
    arr = [list(map(int,input().split())) for _ in range(N)]    # 배열
    find = [list(map(int,input().split())) for _ in range(3)]   # 찾아야하는 배열


    ans = 0     # 일치하는 배열의 갯수
    for i in range(N-3+1):  # 인덱스 값 범위
        for j in range(N-3+1):  # 인덱스 값 범위
            cnt = 0     # arr와 find의 요소가 일치하는 갯수
            if arr[i][j] == find[0][0]:     # 비교 시작 조건
                for k in range(0,3):
                    for l in range(0,3):
                        if arr[i+k][j+l] == find[0+k][0+l]:
                            cnt += 1    # 두 배열이 같은 만큼 +1
            if cnt == 9:    # find의 형태를 arr 속에서 찾는다면
                ans += 1

    print('#{} {}'.format(tc,ans))