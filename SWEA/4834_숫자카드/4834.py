import sys
sys.stdin = open('sample_input.txt','r')

# 테스트 케이스 셋팅
N=int(input())
for test_case in range(1, N+1):
    Len=int(input())    # 숫자 자리수
    num=int(input())    # 숫자

    # 문자열로 입력을 받기 때문에 해당 부분을 먼저 리스트 형태로 만들어줘야 한다.
    # ex. num=12345
    # 배치는 새로 할 것이기 때문에 크게 배치를 생각하지 않고, 리스트를 나눠줘도 괜찮다.

    arr=[0]*Len     # 숫자의 자리수를 쪼개서 넣을 리스트
    n = 0           # n=0으로 설정해두는 이유는 인덱스 값을 적용하기 위해서
    while num!=0:
        arr[n]=num%10       # 일의 자리수가 리스트에 인덱스 값으로 담긴다.
        num = int(num//10)
        n +=1       # 인덱스 값을 하나씩 울려주기 위해서

    # print(arr)
    # 다음으로는 리스트 형태로 분리된 숫자를 새로운 배열에 담아줘야 한다.
    arr_cnt=[0]*10      # 0이 10개 담긴 리스트 생성
    # 해당 리스트를 채우기 위해서는 arr의 숫자들이 몇개 나오는지 찾아줘야 한다.
    for i in arr:
        arr_cnt[i] += 1

    max_cnt = 0
    max_idx = 0
    # 최댓값, 최솟값을 구하기 위해서는 항상 임의로 비교할 숫자를 만들어 줘야 한다.
    for j in range(0,10):
        if max_cnt<=arr_cnt[j]:
            max_cnt = arr_cnt[j]
            max_idx = j

    print('#{} {} {}'.format(test_case, max_idx,max_cnt))


