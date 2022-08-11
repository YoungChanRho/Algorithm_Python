# 4836_색칠하기
# 220811
'''
그림과 같이 인덱스가 있는 10x10 격자에 빨간색과 파란색을 칠하려고 한다.
N개의 영역에 대해 왼쪽 위와 오른쪽 아래 모서리 인덱스, 칠할 색상이 주어질 때, 칠이 끝난 후 색이 겹쳐 보라색이 된 칸 수를 구하는 프로그램을 만드시오.
주어진 정보에서 같은 색인 영역은 겹치지 않는다.


예를 들어 2개의 색칠 영역을 갖는 위 그림에 대한 색칠 정보이다.

2
2 2 4 4 1  ( [2,2] 부터 [4,4] 까지 color 1 (빨강) 으로 칠한다 )
3 3 6 6 2 ( [3,3] 부터 [6,6] 까지 color 2 (파랑) 으로 칠한다 )
'''

import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 주어진 2차원 배열에서 길이랑 좌표값을 아니까 이걸로 접근하고
    # arr[i][4]는 무조건 색깔을 의미
    # arr[i][0:2] / arr[i][2:4]
    # 각각 시작점 좌표와 끝나는 지점의 좌표를 나타낸다.

    bg = [[0]*10 for i in range(10)]
    for j in range(N):
        if arr[j][4] == 1: # 빨간색일 경우
            for k in range(arr[j][0],arr[j][2]+1):    # 행의 높이
                for w in range(arr[j][1],arr[j][3]+1):    # 열의 길이
                    bg[k][w] = 1           # 1로 채운다
                    # 빨간색 부분만 1로 먼저 채워준다.
    
    

    for j in range(N): 
        if arr[j][4] == 2:
            for z in range(arr[j][0],arr[j][2]+1):
                for p in range(arr[j][1],arr[j][3]+1):
                    if bg[z][p] != 0:
                        bg[z][p] = 2
                    # 빨간색이 칠해진 범위 중에 파란색과 겹치는 부분만 2로 칠해준다.
                    # 중복으로 칠해져도 결국 해당 자리에는 2가 들어가서 중복의 문제는 없다고 생각
    cnt = 0 
    for d in range(10):
        for e in range(10):
            if bg[d][e] == 2:
                cnt += 1
                # 전체 배열 속에서 2의 개수가 몇개인지 찾는다.
    print('#{} {}'.format(tc, cnt))