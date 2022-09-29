import sys
sys.stdin = open('input.txt','r')

T = int(input())

right = 1
left = -1
up = -1
down = 1

for tc in range(1,T+1):
    N, M = map(int,input().split())   # N: 배열 M: 뿌리는 방향
    arr = [list(map(int,input().split())) for _ in range(N)]

    max_flies = 0
    # 행 방향
    for i in range(N):
        for j in range(N):
            sumV = 0
            y = i
            x = j
            for k in range(1,M):
                ny_up = y + up*k
                ny_down = y + down*k
                nx_right = x + right*k
                nx_left = x + left*k
                if 0 <= ny_up:
                    sumV += arr[ny_up][x]
                if ny_down <= N-1:
                    sumV += arr[ny_down][x]
                if 0 <= nx_left:
                    sumV += arr[y][nx_left]
                if nx_right <= N-1: 
                    sumV += arr[y][nx_right]
            if sumV + arr[i][j] > max_flies:
                max_flies = sumV + arr[i][j]
    
    for i in range(N):
        for j in range(N):
            sumV = 0
            y = i
            x = j
            for k in range(1,M):
                ny_up = y + up*k
                ny_down = y + down*k
                nx_right = x + right*k
                nx_left = x + left*k
                if 0 <= ny_up and 0 <= nx_left:
                    sumV += arr[ny_up][nx_left]
                if 0 <= ny_up and nx_right <= N-1:
                    sumV += arr[ny_up][nx_right]
                if ny_down <= N-1 and 0 <= nx_left:
                    sumV += arr[ny_down][nx_left]
                if ny_down <= N-1 and nx_right <= N-1:
                    sumV += arr[ny_down][nx_right]
            if sumV + arr[i][j] > max_flies:
                max_flies = sumV + arr[i][j]

    print('#{} {}'.format(tc,max_flies))