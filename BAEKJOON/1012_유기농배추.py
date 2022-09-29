# 상, 우, 하, 좌
dx = [-1, 0, 1, 0]
dy = [0 , 1, 0 ,-1]

# dfs 정의
def dfs(x,y):
    if 0 <= x < V and 0 <= y < H:
        if arr[x][y] == 1:
            arr[x][y] = 2   # 방문한 부분을 2로 변경 
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                dfs(nx,ny)
            return True
        return False
    


T = int(input())    # 케이스 개수
for tc in range(1,T+1):
    V, H, L = map(int,input().split())  # V: 가로, H: 세로, L: 배추 개수
    arr = [[0]*H for _ in range(V)]

    for i in range(L):
        x,y = map(int,input().split())
        arr[x][y] = 1

    cnt = 0
    for i in range(V):
        for j in range(H):
            if arr[i][j] == 1:
                dfs(i, j)
                cnt += 1

    print(cnt)
