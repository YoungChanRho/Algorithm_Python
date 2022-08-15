# 4843_특별한 정렬
# 220811

'''
보통의 정렬은 오름차순이나 내림차순으로 이루어지지만, 이번에는 특별한 정렬을 하려고 한다.
N개의 정수가 주어지면 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로 큰 수와 작은 수를 번갈아 정렬하는 방법이다.
예를 들어 1부터 10까지 10개의 숫자가 주어지면 다음과 같이 정렬한다.
10 1 9 2 8 3 7 4 6 5
주어진 숫자에 대해 특별한 정렬을 한 결과를 10개까지 출력하시오.

첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄에 정수의 개수 N이 주어지고 다음 줄에 N개의 정수 ai가 주어진다. 10<=N<=100, 1<=ai<=100

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 특별히 정렬된 숫자를 10개까지 출력한다.
'''

import sys
sys.stdin = open('input.txt','r')

def bubbleSort(a, arr):
    for i in range(a):
        for k in range(1,a):
            if arr[k-1] >= arr[k]:
                arr[k-1], arr[k] = arr[k], arr[k-1]
    return arr

T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 정수 개수
    ai = map(int,input().split())

    arr = list(ai)
    lst = bubbleSort(N,arr)
    lst_2 = [0]*N
    cnt = 0

    for j in range(N):
        if j%2==0: 
            lst_2[j] = lst[N-1-cnt]
            cnt += 1
        elif j%2==1: 
            lst_2[j] = lst[cnt-1]

    print('#{}'.format(tc), end = " ")
    for i in lst_2[0:10]:
        print(i, end=" ")
    print()


