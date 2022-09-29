paper_count = int(input())  # 색종이 장수
paper_info = [list(map(int,input().split())) for _ in range(paper_count)]
arr = [[0]*101 for _ in range(101)]
# paper_info = [열, 행, 너비, 높이]

for i in range(paper_count):   # 종이 갯수 만큼 반복
                               # 각 인덱스에 숫자를 채워 줌
    for j in range(paper_info[i][0],paper_info[i][0]+paper_info[i][2]):
        # 행 방향, paper_info[i] 같은 경우 문제에서는 반대로 적혀있는데, 의미가 없는 것 같아서 따로 처리없이 가능
        for k in range(paper_info[i][1],paper_info[i][1]+paper_info[i][3]):
            arr[j][k] = i + 1
            # 색 종이 별로 다른 숫자로 체크를 해줘야 한다.
for i in range(paper_count):
    cnt = 0
    for j in arr:
        # arr의 각각의 리스트 속에 색종이에 부여된 번호가 몇개있는가?
        cnt += j.count(i+1)
    print(cnt)


