dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

N, M = map(int,input().split())
arr = [list(map(int,input())) for _ in range(N)]

minn = 9876544321
cnt = 0
visited = [[0]*(M) for _ in range(N)]

def dfs(x,y,cnt):
    global minn
    cnt += 1
    visited[x][y] = 1
    if x == N-1 and y == M-1:
        if cnt < minn:
            minn = cnt
        return
    elif cnt > minn:
        return
    else:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1:
                if visited[nx][ny] != 1:
                    dfs(nx,ny,cnt)
                    visited[nx][ny] = 0
    
dfs(0,0,cnt)
print(minn)


