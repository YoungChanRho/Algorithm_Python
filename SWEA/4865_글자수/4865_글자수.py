# 4865_글자수
# 220816

'''
두 개의 문자열 str1과 str2가 주어진다. 문자열 str1에 포함된 글자들이 str2에 몇 개씩 들어있는지 찾고, 그중 가장 많은 글자의 개수를 출력하는 프로그램을 만드시오.
예를 들어 str1 = “ABCA”, str2 = “ABABCA”인 경우, str1의 A가 str2에 3개 있으므로 가장 많은 글자가 되고 3을 출력한다.
파이썬의 경우 딕셔너리를 이용할 수 있다.

첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트 케이스 별로 길이가 N인 문자열 str1과 길이가 M인 str2가 각각 다른 줄에 주어진다. 5≤N≤100, 10≤M≤1000, N≤M

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''

import sys
sys.stdin = open('sample_input.txt','r')

T = int(input())

for tc in range(1, T +1):
    str1 = input()
    str2 = input()



    str1 = set(str1)
    str1 = list(str1)
    
    
    len_str1 = 0
    for _ in str1:
        len_str1 += 1
    
    len_str2 = 0
    for _ in str2:
        len_str2 += 1

    
    lst = []
    for i in range(len_str1):
        cnt = 0
        for j in range(len_str2):
            if str1[i] == str2[j]:
                cnt +=1
            lst.append(cnt)

    

    len_lst = 0
    for _ in lst:
        len_lst += 1

    maxV = 0
    for i in range(len_lst):
        if lst[i] > maxV:
            maxV = lst[i]


    print('#{} {}'.format(tc, maxV))