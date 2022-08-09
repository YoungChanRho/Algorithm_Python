# 4835_구간합 풀이
# 2022-08-09

import sys
sys.stdin = open('sample_input.txt','r')

# N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하는 것은 디지털 필터링의 기초연산이다.
# M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램을 작성하시오.

# 첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
# 다음 줄부터 테스트케이스의 첫 줄에 정수의 개수 N과 구간의 개수 M 주어진다. ( 10 ≤ N ≤ 100,  2 ≤ M ＜ N )
# 다음 줄에 N개의 정수 ai가 주어진다. ( 1 ≤ a ≤ 10000 )
# ex. 10 3
#     1 2 3 4 5 6 7 8 9 10
#     인접한 3 숫자의 합이 가장 큰 것과 작은 것을 빼준다.

T=int(input())
for test_case in range(1, T+1):
    N, M = map(int,input().split())
    A = list(map(int,input().split()))

    max_sum = 0
    min_sum = 100000000
    idx = 0
    
    for i in range(0, N-M+1):
        sum_num = 0
        # 총 M-N+1 만큼 비교를 한다.
        for j in range(M):
            # 비교 될 값을 만들어줘야하는데, 기준점(덧셈을 시작하는 인덱스)은 계속 1씩 증가를 하고
            # 해당 인덱스로부터 M만큼 인덱스 값을 계속 더해줘야 한다.
            sum_num += A[idx+j]
        if sum_num >= max_sum:
            max_sum = sum_num
        if sum_num <= min_sum:
            min_sum = sum_num
        idx += 1

    ans = max_sum - min_sum

    print('#{} {}'.format(test_case, ans))
