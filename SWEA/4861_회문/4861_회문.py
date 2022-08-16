# 4861_회문
# 220816

'''
ABBA처럼 어느 방향에서 읽어도 같은 문자열을 회문이라 한다. NxN 크기의 글자판에서 길이가 M인 회문을 찾아 출력하는 프로그램을 만드시오.
회문은 1개가 존재하는데, 가로 뿐만 아니라 세로로 찾아질 수도 있다.
예를 들어 N=10, M=10 일 때, 다음과 같이 회문을 찾을 수 있다.

첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트케이스의 첫 줄에 N과 M이 주어진다. 10≤N≤100, 5≤M≤N
다음 줄부터 N개의 글자를 가진 N개의 줄이 주어진다.

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''

import sys
sys.stdin = open('sample_input.txt','r')

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split()) 
    arr = [input() for _ in range(N)]

    ans =[]
    
    for i in range(N):
        for j in range(N-M+1):
            cnt = 0
            if arr[i][j] == arr[i][j+M-1]:   
                cnt += 1
                for k in range(1, M//2):
                    if arr[i][j+k] == arr[i][j+M-1-k]:
                        cnt += 1
                if cnt == M//2:
                    ans = arr[i][j:j+M]
                    continue
                
            
            cnt_1 = 0
            tmp = ''
            if arr[j][i] == arr[j+M-1][i]:
                cnt_1 += 1
                for k in range(1, M//2):
                    if arr[j+k][i] == arr[j+M-1-k][i]:
                        cnt_1 += 1
                if cnt_1 == M//2:
                    for k in range(j,j+M):
                        tmp += arr[k][i]
                    ans = tmp
                                
    print('#{} {}'.format(tc, ans))

    