N = int(input())
find_num = int(input())
arr = [[0]*N for _ in range(N)]

# 하, 우, 상, 좌
dy = [1, 0, -1, 0]  # 행 방향
dx = [0, 1, 0, -1]  # 열 방향

arr[0][0] = N**2    # 처음 시작값을 할당해 준다.

y = 0   # 행 방향 움직임
x = 0   # 열 방향 움직임

direction = 0  # 방향을 변경해 줄 변수

cnt = 1

if find_num == N**2:
    ans1 = 1
    ans2 = 1
else:
    ans1 = 0
    ans2 = 0

# (N**2) - 1 만큼 반복 진행  
for i in range(1,N**2):
    # 방향이 반영된 새로운 인덱스
    ny = y + dy[direction%4]
    nx = x + dx[direction%4]
    if 0 <= ny < N and 0 <= nx < N: # 인덱스가 범위를 벗어나지 않을 경우
        if arr[ny][nx] == 0:    # 다음번째 숫자가 0 인 경우
            y = ny  # y값 초기화
            x = nx  # x값 초기화
            arr[y][x] = (N**2) - cnt    # 숫자 넣어주기
            if arr[y][x] == find_num:
                ans1 = y+1
                ans2 = x+1
            cnt += 1
        elif arr[ny][nx] != 0:   # 숫자가 이미 채워져 있는 경우, 방향 변경
            direction += 1
            ny = y + dy[direction%4]
            nx = x + dx[direction%4]
            y = ny
            x = nx
            arr[y][x] = (N**2) - cnt
            if arr[y][x] == find_num:
                ans1 = y+1
                ans2 = x+1
            cnt += 1
    else:   # 인덱스가 범위를 벗어날 경우 방향 전환
        direction += 1
        ny = y + dy[direction%4]
        nx = x + dx[direction%4]
        y = ny
        x = nx
        arr[y][x] = (N**2) - cnt
        if arr[y][x] == find_num:
            ans1 = y+1
            ans2 = x+1
        cnt += 1

for i in range(N):
    for j in range(N):
        print(arr[i][j], end= " ")
    print()

print(ans1, ans2)
