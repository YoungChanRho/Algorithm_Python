# 카운팅 정렬 
def CountingSort(lst):
     # lst의 길이 구해주기
    len = 0
    for _ in lst:
        len += 1

    # lst의 최대값 구해주기
    maxV = 0    # lst의 최대값
    for i in range(len):
        if lst[i] > maxV:
            maxV = lst[i]

    # 0으로 차있는 리스트 만들어주기
    C = [0]*(maxV+1)
   
    for a in lst:
        C[a] += 1
    
    for i in range(1, maxV+1):
        C[i] += C[i-1]

    # 최종 배열 진행
    result = [0]*(len)

    for i in lst:
        result[C[i]-1] = i
        C[i] -= 1
    
    return result

# 난쟁이 정보 입력 받기
lst = [input() for _ in range(9)]

# couunting sort에서 정수간의 비교가 필요하기 때문에 list안의 요소들을 정수로 변경
int_lst = list(map(int,lst))

# 정열을 진행한 난쟁이 키 리스트
C_int_lst = CountingSort(int_lst)

# 난쟁이들 키의 합
sumV = 0
for i in int_lst:
    sumV += i

# 가짜 난쟁이 둘의 키를 합쳤을 때 나올 수
fake = sumV - 100

# 가짜 난쟁이 중 키가 큰 녀석의 수로 fake를 나눌 경우, 그 나머지는 다른 한명의 키가 돼야 함
# 난쟁이들의 키를 뒤에서부터 탐색 (큰 순서대로)
a = 0   # 키가 큰 가짜 난쟁이
b = 0   # 키가 작은 가짜 난쟁이
for i in C_int_lst[::-1]:
    F = fake % i
    if (fake//i == 1) and F in C_int_lst:   # 키 큰 난쟁이로 Fake를 나눴을 때 몫이 1이고, 그 나머지가 C_int_list에 있다면
        a = i   # 키 큰 가짜 난쟁이 키 할당
        b = F   # 키 작은 가짜 난쟁이 키 할당

# 해당 키를 가진 난쟁이들 리스트에서 제거
C_int_lst.remove(a)
C_int_lst.remove(b)

# 출력
for i in C_int_lst:
    print(i)

# 난쟁이 간의 키에 있어서 중복이 없다는 조건이 있었기에 해당 풀이가 가능했다고 생각
