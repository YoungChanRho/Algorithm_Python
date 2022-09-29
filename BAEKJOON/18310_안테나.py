N = int(input())    # 집의 개수
home = list(map(int,input().split()))   # 집의 위치
home = sorted(home)
print(home[(N-1)//2])
