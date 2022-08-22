import sys
sys.stdin = open('algo1_sample_in.txt','r')

T = int(input())

for  tc in range(1, T+1):

    line_len = int(input())     # 행의 갯수
    point_s_e = list(map(int,input().split()))    # 평탄화 시작 및 종료 좌표
    arr = [list(map(int,input().split())) for _ in range(line_len)]     # 배열 입력


    area_size = (point_s_e[2] - point_s_e[0]+1) * (point_s_e[3] - point_s_e[1]+1)    # 영역 칸 수
    
    area_height = 0    # 높이 합
    for i in range(point_s_e[0],point_s_e[2]+1):
        for j in range(point_s_e[1], point_s_e[3]+1):
            area_height += arr[i][j]

    area_avg = int(area_height // area_size)    # 평균값, 평탄화 값

    cnt = 0     # 평탄화 횟수

    while True:

        sum_area_2 = 0      # arr의 요소값 변화에 따른 높이의 합 변화
        for i in range(point_s_e[0],point_s_e[2]+1):
            for j in range(point_s_e[1], point_s_e[3]+1):
                sum_area_2 += arr[i][j]


        for i in range(point_s_e[0],point_s_e[2]+1):
            for j in range(point_s_e[1], point_s_e[3]+1):
         
                # area_avg(평탄화 값)에 맞춰 배열 값 변화
                if arr[i][j] < area_avg:    # area_avg보다 작다면
                    arr[i][j] += 1
                    cnt += 1
                    continue
                elif arr[i][j] == area_avg: # area_avg와 같다면
                    pass
                elif arr[i][j] > area_avg:  # area_avg보다 크다면
                    arr[i][j] -= 1 
                    cnt += 1
                    continue
                
        if sum_area_2 == area_size*area_avg:
            break
    
    
    print('#{} {}'.format(tc,cnt))
