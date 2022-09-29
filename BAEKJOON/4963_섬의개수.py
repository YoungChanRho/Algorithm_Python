import sys
sys.setrecursionlimit(5000000)

# 좌상, 상, 우상, 우, 우하, 하, 좌하, 좌
dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

# x,y -> dsf시작 좌표
def dfs(x,y):
    if 0 <= x < h and 0 <= y < w:   # 인덱스가 범위 내에 있을 경우
        if arr[x][y] == 1:  # 섬의 시작점을 찾을 경우
            arr[x][y] =2    # 방문 표시를 위해 숫자를 2로 변경해 준다.
            for i in range(8):  # 모든 방향 확인을 위해
                nx = x + dx[i]
                ny = y + dy[i]
                dfs(nx,ny)      # 재귀를 통해 확인
            return True
        return False            # 범위에 맞지 않을 경우 False         


while True:
    w, h = map(int,input().split()) # 넓이, 높이를 입력 받는다.

    if w == 0 and h == 0:   # w, h가 0일 경우, 중단
        break
    
    
    arr = [list(map(int,input().split())) for _ in range(h)]    # 배열을 입력 받는다.

    cnt = 0 # 섬 개수를 구한다.
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                dfs(i,j)
                cnt += 1
    print(cnt)
