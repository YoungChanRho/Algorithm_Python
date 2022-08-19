'''
1. 산술평균: N개의 수들의 합을 N으로 나눈 값 (소수점 이하 첫째자리에서 반올림한 값을 출력)
2. 중앙값: N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
3. 최빈값: N개의 수들 중 가장 많이 나타나는 값
4. 범위: N개의 수들 중 최댓값과 최솟값의 차이
'''

N = int(input())    # 입력되는 숫자들의 갯수

lst = [input() for _ in range(N)]  # 입력 되는 숫자를 리스트 형태로 받는다.
lst = list(map(int, lst))


# 산술 평균
def arithmetic_mean(N,lst):
    sum = 0
    for i in lst:
        sum += i
    K = sum/N
    return round(K)

# 중앙값
def mid(N,lst):
    for i in range(N):
        for k in range(1, N-1):
            if lst[k] > lst[k+1]:
                lst[k], lst[k+1] = lst[k+1],lst[k]
    return lst[N//2]

# 최빈값
# 아직 해결 못 함
# 셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
# 최빈값이 여러 개 있을 경우 최빈값 중 두 번째로 작은 값을 출력한다.
# 최빈값 같은 경우 set을 통해 중복을 제거해주고
# 다시 list로 만든 뒤, 각각의 값들이 몇번 나오지는 찾은 후 max를 구하면 될 것 같은데
# 중복이 발생할 시 어떻게 처리를 해야할지 모르겠다 ..
# 풀이 진행 중 .. 

def frequency(N,lst):
     # 중복제거
    lst = set(lst)
    lst = list(list)
    num_list = []  # 각 숫자들이 몇번 나오는지 나타나는 리스트
    
    for i in lst:
        cnt = 0
        for j in range(N):
            if i == lst[j]:
                cnt += 1
        num_list.append(cnt)
    
    maxV = 0
    idx = 0

    for i in range(num_list):
        if num_list[i] > maxV:
            maxV = num_list[i]
            idx = i
            
    return lst[idx]
    # 최빈값을 구하는 방법
    # 중복이 발생할시 어떻게 처리해야할까?




# 범위

def max_min(N,lst):
    maxV = 0
    minV = 1000000000
    for i in range(N):
        if lst[i] > maxV:
            maxV = lst[i]
        if lst[i] < minV:
            minV = lst[i]
    
    max_min = maxV - minV
    return max_min


print(arithmetic_mean(N,lst))
print(mid(N,lst))
print(max_min(N,lst))