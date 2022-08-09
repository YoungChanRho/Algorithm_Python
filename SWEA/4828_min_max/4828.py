import sys
sys.stdin = open('sample_input.txt','r')

# N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.
# 첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 50 )
# 각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 1000 )
# 다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 1000000 )

T=int(input())

for test_case in range(1, T+1):
    N = int(input())
    A = list(map(int,input().split()))

    # list(A)에서 최대값과 최소값을 구해야 한다.
    # ex. A = [477162, 658880, 751280, 927930, 297191]
    min_num = 1000000
    max_num = 0
    idx = 0
    # index값은 최솟값과 최대값 구할 때 모두 계속 증가하여야 하므로 따로 두개를 두지 않아도 된다..?
    for i in A:
        if max_num <= A[idx]:
            max_num = A[idx]
        if min_num >= A[idx]:
            min_num = A[idx]
        idx += 1

    ans = max_num - min_num

    print('#{} {}'.format(test_case, ans))
