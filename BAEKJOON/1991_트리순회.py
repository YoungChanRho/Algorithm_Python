# 전위순회
def preorder(parent):
    if parent == '.':   # 노드가 없으면 이전 단계로 이동
        return
    print(parent, end = "")    # 처음에 부모 노드를 찍고
    preorder(tree[parent][0])    # 왼쪽 자식 노드 확인
    preorder(tree[parent][1])    # 오른쪽 자식 노드 확인
# 중위순회
def inorder(parent):
    if parent == '.':
        return
    inorder(tree[parent][0])
    print(parent, end="")
    inorder(tree[parent][1])
# 후위순회
def postorder(parent):
    if parent =='.':
        return
    postorder(tree[parent][0])
    postorder(tree[parent][1])
    print(parent, end ='')

N = int(input())
# 트리 형식으로 담을 수 있다.
tree = {}

for _ in range(N):
    # 부모노드와 자식 노드를 따로 저장
    parent, left, right =input().split()
    tree[parent] = left, right
    tree_key = list(tree.keys())

preorder(tree_key[0])
print()
inorder(tree_key[0])
print()
postorder(tree_key[0])
print()