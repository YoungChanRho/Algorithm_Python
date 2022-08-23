# # 1219_길찾기
# # 220823

import sys
sys.stdin = open('input.txt','r')

def my_dfs(my_graph, start_node):
    visited = []    # 방문한 곳 표시
    stack = []      # 방문 예정인 곳 표시
    stack.append(start_node)    # stack에 시작점을 먼저 담아준다.
    
    while stack:    # stack이 비어있지 않다면
        node = stack.pop()  # node = stack[-1] 을 해주는 동시에 stack[-1] -> pop
        if node not in visited: # stack[-1]이 방문하지 않았던 곳이라면 
            visited.append(node)    # 해당 node를 방문
            stack.extend(my_graph[node])    # 해당 node에서 갈 수 있는 장소들을 stack에 추가
    
    # stack에 모든게 pop되면, while문 탈출
    return visited

for tc in range(1,11):
    T, line = map(int,input().split())  # 테스트 케이스 번호, 길의 갯수
    lst = list(map(int,input().split()))    # my_graph를 만들 정보를 담은 리스트

    key_lst = []    # key 값을 담은 lst / 출발 가능 노드
    value_lst = []  # value 값을 담은 lst / 도착 가능 노드

    len_lst = 0     # key_lst와 value_lst를 만들어주기 위해
    for _ in lst:
        len_lst += 1

    for i in range(len_lst):
        if i % 2 == 0:  # 짝수일 경우 출발 노드 
            key_lst.append(lst[i])
        else:           # 홀수일 경우 도착 노드
            value_lst.append(lst[i])

    my_graph_lst = [[] for _ in range(100)] # 노드는 총 100개까지 가능

    for i in range(len_lst//2):     # len_lst//2를 해준 이유는 key_lst와 value_lst에 홀,짝을 나누어서 담아줬기 때문
        my_graph_lst[key_lst[i]].append(value_lst[i])


    if 99 in my_dfs(my_graph_lst, 0):
        print('#{} 1'.format(T))
    else:
        print('#{} 0'.format(T))
