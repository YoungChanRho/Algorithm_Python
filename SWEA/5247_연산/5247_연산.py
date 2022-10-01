import sys
sys.stdin = open('input.txt','r')
from collections import deque

# dfs 정의
def bfs():
    # 변화하는 값(N)에 따른 cnt의 변화를 튜플의 형태로 deque에 넣어준다.
    q = deque([(N,0)])
    # 연산 결과가 백만 이하를 넘을 수 없기 때문에
    # q에 원소가 있을 경우
    while q:
        # 작업을 진행해줄 값인 summ 값과 cnt값을 꺼낸다.
        summ, cnt = q.popleft()
        # 해당 값을 방문한 적이 있다면
        if visited[summ]:
            continue
        # 방문하지 않았다면 방문처리를 해준다.
        visited[summ] = 1
        # summ 값이 목표하는 값과 같아진다면
        # cnt를 return하고 함수를 종료한다.
        if summ == M:
            return cnt
        cnt += 1
        # 모든 연산을 한번씩 진행해준다.
        # 연산의 결과는 자연수이며, 백만 이하여야 한다.
        # 모든 경우를 수행해야 하기 때문에 elif가 아닌 if문을 전부 걸어준다.
        if 0 < summ - 1 <= 10**6:
            q.append((summ-1,cnt))
        if 0 < summ + 1 <= 10**6:
            q.append((summ+1,cnt))
        if 0 < summ*2 <= 10**6:
            q.append((summ*2, cnt))
        if 0 < summ - 10 <= 10**6:
            q.append((summ-10,cnt))

T = int(input())

for tc in range(1, T+1):
    N, M = map(int,input().split())
    # vistied를 백만을 최대 크기로 잡아 생성한다.
    visited = [0]*(10**6+1)
    ans = bfs()
    print("#{} {}".format(tc, ans))