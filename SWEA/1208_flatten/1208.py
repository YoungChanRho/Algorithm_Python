import sys
sys.stdin = open('input.txt','r')

# 덤프 = 가장 높은 값에서 -1을 해주고, 가장 낮은 값에 + 1 을 해주는 것
# 평탄화가 완벽하게 될 경우 0 또는 1을 반환

for test_case in range(1, 10+1):
    D = int(input())        # 덤프 횟수
    lst = list(map(int,input().split()))        # 상자 높이

    # 상자 높이 리스트에서 최댓값과 최솟값을 구해주고 dump 횟수 만큼 반복문을 사용해서 최댓값에서는 -1을, 최솟값에서는 +1을 진행한다.
    # 만일, dump를 진행중에 (최댓값 - 최솟값)의 차이가 0 또는 1이 나오면, 진행을 중단하고 높이 차를 반환한다.
    # 그렇다면 계속해서 중간 중간에 높이차를 확인해 줘야한다.
    # 먼저 최대값과 최소값을 구하자
    
    for i in range(D):      
        # D 만큼 돈다.
        # 평탄화 작업
        # 새로운 리스트를 만들어주는 과정
        # 해당 for 문이 끝나면 평탄화가 완료 된 lst가 만들어진다
        max_num=0
        max_idx=0
        min_num=100
        min_idx=0
        for j in range(100):
            if lst[j] >= max_num:
                max_num = lst[j]
                max_idx = j
            if lst[j] <= min_num:
                min_num = lst[j]
                min_idx = j
            
        if (max_num - min_num == 0) or (max_num - min_num == 1):
            break
        # 평탄화 작업 중 max_num 과 min_num의 차이가 0 또는 1이 발생하면 평탄화를 중단한다.
        max_num = max_num - 1 
        min_num = min_num + 1
        lst[max_idx] = max_num
        lst[min_idx] = min_num
    

       
    max_num = 0
    min_num = 100

    for k in range(100):
        if lst[k] >= max_num:
            max_num = lst[k]
        if lst[k] <= min_num:
            min_num = lst[k]
        
       
        
    print('#{} {}'.format(test_case,(max_num-min_num)))