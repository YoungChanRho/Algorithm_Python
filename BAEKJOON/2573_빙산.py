# 상, 좌, 하, 우
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


# 섬을 둘러싼 사방이 0이기 때문에, 인덱스 범위를 벗어나는 것에 대해서는 고려할 필요 없다.
# 나중에 for문을 통해서 처리해주면 된다.
def find(x,y):
    global height
    global width

    if 0 <= x < height and 0 <= y < width:  # 범위 내에 있다면
        if arr[x][y] != 0:
            
            



height, width = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(height)]

