# 4871_그래프경로
# 220823
import sys
sys.stdin = open('input.txt','r')

def my_dfs(my_graph, start_node):   # dfs 함수 정의
    visit = []  # 방문한 node
    stack = []  # 앞으로 방문할 node
    stack.append(start_node)    # 탐색 시작 node를 stack에 담아준다.

    while stack:    # 방문할 node들이 남아 있다면
        node = stack.pop()  # stack.pop을 해주고, 해당 값을 node에 담아준다.
        if node not in visit:   # 방문하려고 탐색하는 node가 아직 방문하지 않은 곳 이라면
            visit.append(node)  # 방문 리스트에 삽입
            stack.extend(my_graph[node])    # 새로 방문한 node로 부터 방문할 수 있는 새로운 node를 stack에 추가
        # node가 이미 방문한 곳 이라면 그냥 pop을 진행하고, while문을 다시 순회
    return visit

T = int(input())

for tc in range(1,T+1):
    V, E = map(int,input().split())     # V = 노드 개수  /  E = 간선 개수
    node_info = [list(map(int,input().split())) for _ in range(E)]      # 노드 연결 정보를 이차원 배열로 받는다.
    start_node, end_node = map(int,input().split())

    my_graph = [[] for _ in range(50)]  # 각각의 node로부터 이동가능한 node들을 표현

    for i in range(E):  # 간선 개수가 곧 이동 가능 정보
        my_graph[node_info[i][0]].append(node_info[i][1])

    if end_node in my_dfs(my_graph, start_node):
        print('#{} 1'.format(tc))
    else:
        print('#{} 0'.format(tc))
