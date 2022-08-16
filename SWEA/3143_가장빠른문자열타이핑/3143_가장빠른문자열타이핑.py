# 3143_가장빠른 문자열 타이핑
# 220816

'''
어떤 문자열 A를 타이핑하려고 한다.
그냥 한 글자씩 타이핑 한다면 A의 길이만큼 키를 눌러야 할 것이다.
여기에 속도를 조금 더 높이기 위해 어떤 문자열 B가 저장되어 있어서 키를 한번 누른 것으로 B전체를 타이핑 할 수 있다.
이미 타이핑 한 문자를 지우는 것은 불가능하다.
예를 들어 A=”asakusa”, B=”sa”일 때, 다음 그림과 같이 B를 두 번 사용하면 5번 만에 A를 타이핑 할 수 있다.

A와 B가 주어질 때 A 전체를 타이핑 하기 위해 키를 눌러야 하는 횟수의 최솟값을 구하여라.

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스마다 첫 번째 줄에 두 문자열 A, B가 주어진다. A의 길이는 1이상 10,000이하, B의 길이는 1이상 100이하이다.

각 테스트 케이스마다 A 전체를 타이핑 하기 위해 키를 눌러야 하는 횟수의 최솟값을 출력한다.
'''

import sys
sys.stdin = open('sample_input.txt','r')


T = int(input())

for tc in range(1,T+1):
    A, B = input().split()      # 입력

    # B가 A에 몇개 들었는지 갯수를 찾아주고, 해당 갯수만큼 전체의 길이에서 빼주고 갯수를 더해주면 된다.
    # 먼저 A가 몇개있는지 찾아준다.
    
    # A의 길이
    len_A = 0
    for _ in A:
        len_A += 1


    # B의 길이
    len_B = 0
    for _ in B:
        len_B += 1


    abs_cnt = 0
    for i in range(len_A-len_B+1):
        cnt = 0            
        if B[0] == A[i]:
            cnt += 1
            for j in range(1, len_B):
                if B[0+j] == A[i+j]:
                    cnt += 1
            if cnt == len_B:
                abs_cnt += 1
    
    fin_ans = len_A - abs_cnt*len_B+ abs_cnt
    print('#{} {}'.format(tc, fin_ans))