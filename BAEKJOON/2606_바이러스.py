def dfs(start, new_arr):
    stack = []
    visited = []    # 방문한 곳
    stack.append(start)
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(new_arr[node])
    return visited
            

computer_count = int(input())
connected = int(input())
arr = [list(map(int,input().split())) for _ in range(connected)]

# print(arr)

new_arr = [[] for _ in range(computer_count+1)] # 각 노드에 연결된 노드를 나타내는 배열

for i in range(connected):
    new_arr[arr[i][0]].append(arr[i][1])
    new_arr[arr[i][1]].append(arr[i][0])

    # 길 찾기의 경우, 일방이여도 문제 X 

print(len(dfs(1,new_arr))-1)
# print(dfs(1,new_arr))

# dfs로 풀이를 했는데, 일방향으로 할 경우 풀릴 것이라고 생각했는데
# 왜 꼭 양방향으로 해야하는지 잘 모르겠다.
# 결국 visited는 똑같이 나올 것이라고 생각
