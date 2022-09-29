def dfs(my_graph,start_node):
    stack = []
    visit = []
    stack.append(start_node)
    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(my_graph[node])
    return visit

def bfs(my_graph, start_node, N):
    visit = [0]*(N+1)
    queue = []
    queue.append(start_node)
    visit[start_node] = 1
    ans = []
    while queue:
        t = queue.pop(0)
        ans.append(t)
        for i in my_graph[t]:
            if not visit[i]:
                queue.append(i)
                visit[i] = visit[i]+1
    return ans

    

T =int(input())
for tc in range(1,T+1):
    N, M, V = map(int,input().split())  # N: 정점 개수, M: 간선 개수, V: 시작 정점

    my_graph = [[] for _ in range(N+1)]
    for i in range(M):
        a, b = map(int,input().split())
        my_graph[a].append(b)
        my_graph[b].append(a)

    for i in dfs(my_graph,V):
        print(i, end= ' ')
    print()
    for i in bfs(my_graph,V,N):
        print(i, end= ' ')
    print()
