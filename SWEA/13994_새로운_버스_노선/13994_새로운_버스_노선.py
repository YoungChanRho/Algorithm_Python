import sys
sys.stdin = open('input.txt','r')

'''
정류장은 1 ~ 1000번까지 번호가 부여되어 있음
각 노선은 A에서 B번 정류장까지 다음 규칙에 의해 운영
모든 버스 A에서 출발, B까지 운행, 즉, A와 B에 반드시 정차
일반버스 -> A, B 사이의 모든 정류장에 정차
급행버스 -> A가 짝수인 경우 -> A,B사이의 모든 짝수 번호 정류장에 정차
       -> A가 홀수인 경우 -> A,B사이의 모든 홀수 번호 정류장에 정차
광역 급행 버스 -> A가 짝수인 경우 -> A,B 사이의 모든 4의 배수 번호 정류장에 정차
            -> A가 홀수인 경우 -> A,B 사이의 3의 배수이면서, 10의 배수가
            아닌 번호 정류장에 정차

버스 종류와 A, B 에 대한 정보가 주어질 때, 최대 몇 개의 노선이 같은 정류장에 정차하는지?
'''

T = int(input())

for tc in range(1,T+1):
    bus_count = int(input())
    bus_info = [list(map(int,input().split())) for _ in range(bus_count)]
    
    bus_stop_lst = [0]*1001 # 각 각의 버스 노선이 멈추는 횟수를 추가해주고 최대값을 구하면 된다.

    for i in range(bus_count):  # 일반 버스
        bus_stop_lst[bus_info[i][1]] += 1
        bus_stop_lst[bus_info[i][2]] += 1

        if bus_info[i][0] == 1:
            for j in range(bus_info[i][1]+1,bus_info[i][2]):
                bus_stop_lst[j] += 1

        elif bus_info[i][0] == 2:   # 급행 버스
            if bus_info[i][1] % 2 == 0:
                for k in range(bus_info[i][1]+1,bus_info[i][2]):
                    if k%2 == 0:
                        bus_stop_lst[k] += 1
            else:
                for l in range(bus_info[i][1]+1,bus_info[i][2]):
                    if l%2 == 1:
                        bus_stop_lst[l] += 1

        elif bus_info[i][0] == 3:
            if bus_info[i][1]%2 == 0:
                for m in range(bus_info[i][1]+1,bus_info[i][2]):
                    if m%4 == 0:
                        bus_stop_lst[m] += 1
            else:
                for n in range(bus_info[i][1]+1,bus_info[i][2]):
                    if ((n%3 == 0)and(n%10 != 0)):
                        bus_stop_lst[n] += 1

    print('#{} {}'.format(tc,max(bus_stop_lst)))
