N = int(input())
students = []
for i in range(N):
    students.append(list(map(int,input().split())))
    # 학생 수를 입력받고, 해당 줄 만큼 리스트의 형태로 학생들의 반을 입력 받음


list_1 = []
#각 학생들이 어떤 학생들과 같은 반이었는지 set형태로 넣어줌
for j in range(N):
    # cnt = 0
    result=set()
    # 학생들이 중복해서 등장해도 한번으로 처리하기 때문에, set을 사용
    for k in range(5):
        for w in range(N):
            if students[j][k] == students[w][k]:
                result.add(w)
                # 학생이 등장 할 경우 set에 추가
    list_1.append(result)
    # 각 학생의 같은 반이 되었던 친구들의 목록을 set형태로 리스트에 추가

list_2=[]
for i in range(N):
    list_2.append(len(list_1[i]))
    # len을 통해 set의 길이를 구해줌, set의 길이가 가장 긴 사람이 같은 반이 되었던 친구가 가장 많은 학생
    # but? 같은 반을 한번 한 친구와 한번도 해보지 못한 친구가 둘다 len(set)의 값이 1로 나올텐데 그 경우 어떻게 처리해줘야할지 모르겟음
    # 예를 들어 다 다른 반을 했고 학생들이 그중 두명의 학생만 서로 같은 반을 했을 경우
    
    # 5 5 5 5   len(set) = 1 
    # 2 1 1 1   len(set) = 1
    # 3 4 4 4   len(set) = 1
    # 2 7 7 7   len(set) = 1
    
    # 이런식으로 나오는데, 실상 반장이 되어야 할 사람은 2번 학생인데, 1번 학생이 선택되는 경우가 발생하지 않을까?
    # 답은 맞았는데, 해당 경우를 어떻게 처리해 줘야할지 모르겠음.


print(list_2.index(max(list_2))+1)

# 반장이 될 수 있는 학생이 여러명 발생할 경우 가장 빠른 순번의(인덱스 값) 학생을 반장으로 선택하라고 했는데
# max를 사용할 경우, max값에 해당하는 값 중 인덱스 순서가 가장 빠른걸 반환하므로 반장 중복 선택 해결 가능


# 잘 못 이해 했을 때 짠 코드.
#                 cnt += 1
#     list_1.append(cnt-5)
# print(list_1)
# m = max(list_1)
# print(m)
# f = list_1.index(m)
# print(f+1)
