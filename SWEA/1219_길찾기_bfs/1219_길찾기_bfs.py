import sys
sys.stdin = open('input.txt','r')

def bfs(v,N, t):   # v: 시작점, N: 마지막 정점  t: 찾는 정점
    visited = [0]*(N+1)
    q = []
    q.append(v) # q에 v를 넣어준다.
    visited[v] = 1  # 시작 정점 방문 표시
    while q:    # q가 있다면
        v = q.pop(0)
        if v == t:
            return 1    # 목표 발견
        for i in adj_line[v]:
            if visited[i] != 1: # 만약 방문 목록에 해당 정점으로부터
                q.append(i)
                visited[i] = visited[v] + 1

    return 0

T = 10
for tc in range(1,T+1):
    tc, E = map(int,input().split())    # 테스트 케이스 입력받고, 간선 갯수
    line = list(map(int,input().split()))   # input 파일 입력받음
    adj_line = [[] for _ in range(100)]

    # 짝수번째 인덱스가 시작점을 의미하고
    # 홀수번째 인덱스가 시작점으로부터 이동이 가능한 도착점을 의미
    for i in range(len(line)):
        if i % 2 == 0:      # 인덱스가 짝수 번째라면, line[i]는 adj_line의 이차원 배열의 인덱스를 의미한다.
            adj_line[line[i]].append(line[i+1]) # 이렇게 해두면 단방향 배열만 만들어진다.

    print(f'#{tc} {bfs(0, 99, 99)}')