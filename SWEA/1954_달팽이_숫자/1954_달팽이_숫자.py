# 1954_달팽이_숫자
# 220819
import sys
sys.stdin = open('input.txt','r')


T = int(input())
# 우, 하,좌, 상
dy = [0,1,0,-1] # 열 방향
dx = [1,0,-1,0] # 행 방향

for tc in range(1,T+1):
    N = int(input())    # N*N
    arr = [[0]*N for _ in range(N)]     # 0으로 찬 배열 만들어주기

    num = 2 # 배열에 들어갈 값
    direction = 0   # 0,1,2,3 을 벗어나면 안된다.
    arr[0][0] = 1
    y = 0   # 열 방향 인덱스
    x = 0   # 행 방향 인덱스

    for i in range((N**2)-1):   # 반복문 횟수
        ny = y + dy[direction%4]
        nx = x + dx[direction%4]
        if 0<=ny<N and 0<=nx<N: # 만약 새로운 인덱스 값이 인덱스 범위를 벗어나지 않는다면
            if arr[ny][nx] == 0:    # 다음 칸이 0 이라면
                arr[ny][nx] = num   # 숫자를 삽입
                num += 1
                y = y + dy[direction%4] # 행값 변경
                x = x + dx[direction%4] # 열값 변경
            else:   # 숫자를 채워 가던 중, 0이 아닌 수를 만나면 방향 변경
                direction += 1  # 방향 변경
                ny = y + dy[direction%4]
                nx = x + dx[direction%4]
                arr[ny][nx] = num
                num += 1
                y = y + dy[direction%4]
                x = x + dx[direction%4]
        else:   # 새로운 인덱스 값이 범위를 벗어난다면
            direction += 1  # 방향 변경
            ny = y + dy[direction%4]
            nx = x + dx[direction%4]
            arr[ny][nx] = num
            num += 1
            y = y + dy[direction%4]
            x = x + dx[direction%4]

    print('#{}'.format(tc))
    for i in range(N):
        for j in range(N):
            print(arr[i][j],end = ' ')
        print()
