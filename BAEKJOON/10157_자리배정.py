# 상, 우, 하, 좌 방향
dy = [-1,0,1,0]
dx = [0,1,0,-1]

C, R = map(int, input().split())    # C: 열  R: 행
waiting_number = int(input())       # 대기 번호
concert_hall = [[0]*C for _ in range(R)]    # 전체 배열, 공연장 크기

direction = 0   # 방향 변경
y = R-1     # R, 행
x = 0       # C, 열
concert_hall[y][x] = 1  # 시작 값
num = 2

if waiting_number == 1: # 대기번호 = 1인 경우
    print(1,1)
elif 2<=waiting_number<=C*R:  # 대기 번호가 유효할 경우
    for i in range(C*R-1):
        ny = y + dy[direction%4]
        nx = x + dx[direction%4]
        if 0<=nx<C and 0<=ny<R:     # 인덱스가 옳바른 범위 내에 있다면
            if concert_hall[ny][nx] == 0:
                concert_hall[ny][nx] = num
                num += 1
                y = ny
                x = nx
                if num-1 == waiting_number:
                    print(nx+1,R-ny)
                    break
            else:
                direction += 1
                ny = y + dy[direction%4]
                nx = x + dx[direction%4]
                concert_hall[ny][nx] = num
                num += 1
                y = ny
                x = nx
                if num-1 == waiting_number:
                    print(nx+1,R-ny)
                    break
        else:   # 인덱스 범위를 벗어난다면
            direction += 1
            ny = y + dy[direction%4]
            nx = x + dx[direction%4]
            concert_hall[ny][nx] = num
            num += 1
            y = ny
            x = nx
            if num-1== waiting_number:
                print(nx+1,R-ny)
                break
else:   # 유효하지 않은 대기번호일 경우
    print(0)

