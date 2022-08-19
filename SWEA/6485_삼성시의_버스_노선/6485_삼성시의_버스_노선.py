# 6485_삼성시의_버스_노선
# 220819

import sys
sys.stdin = open('input.txt','r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())    # 버스 노선의 수
    bus_road = [list(map(int,input().split())) for _ in range(N)]   # i번째 버스 노선의 이동 정류장
    P = int(input())    # 정류장의 개수(노선이 지나다니는)
    bus_stop = [input() for _ in range(P)]
    bus_stop = list(map(int,bus_stop))  # 정수 변환

    answer_list = [0]*(P)    # 특정 정류장을 지나가는 노선의 수가 담길 리스트
    
    for i in range(N):  # 노선 개수
        for j in range(P):  # 정류장 개수
            if bus_road[i][0] <= bus_stop[j] <= bus_road[i][1]: # bus_stop이 노선 경로 안에 존재한다면, answer_list에 +1
                answer_list[j] += 1

    
    
    #출력
    
    print('#{}'.format(tc), end= ' ')   

    for i in range(P):
        print(answer_list[i], end= ' ')
    print()

    # end = ' ' 사용할 경우, 공백부터 뒤로 다시 출력한다.
    # print()를 찍어서 줄을 넘겨줘야 쭉 나온다.