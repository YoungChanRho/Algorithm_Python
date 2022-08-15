# 1213_string
# 220812

'''
주어지는 영어 문장에서 특정한 문자열의 개수를 반환하는 프로그램을 작성하여라.
Starteatingwellwiththeseeighttipsforhealthyeating,whichcoverthebasicsofahealthydietandgoodnutrition.
위 문장에서 ti 를 검색하면, 답은 4이다.

총 10개의 테스트 케이스가 주어진다.
문장의 길이는 1000자를 넘어가지 않는다.

한 문장에서 검색하는 문자열의 길이는 최대 10을 넘지 않는다.
한 문장에서는 하나의 문자열만 검색한다. 
각 테스트 케이스의 첫 줄에는 테스트 케이스의 번호가 주어지고 그 다음 줄에는 찾을 문자열, 그 다음 줄에는 검색할 문장이 주어진다.

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 답을 출력한다.
'''
import sys
sys.stdin = open('test_input.txt','r',encoding='utf-8')

for tc in range(1,11):
    N = int(input())
    find = input()
    reference = input()

    # 찾아야 하는 문자열의 길이
    len_find = 0
    for _ in find:
        len_find += 1
    
    # 총 문자열의 길이
    len_reference = 0
    for _ in reference:
        len_reference += 1

    cnt = 0     # 정답 담을 변수
    for i in range(len_reference-(len_find-1)):    # 총 문자열에서 탐색 문자열의 길이 만큼 빼준다.
        if find[0] == reference[i]:     # 만약 탐색 문자열의 첫글자와 총문자열에서의 글자 중 일치하는 것이 발생한다면
            cnt_1 = 0
            for j in range(1, len_find):    # 그 뒤의 문자들을 비교
                if find[0+j] == reference[i+j]: # 만약 뒤의 문자들이 동일하다면
                   cnt_1 += 1  # cnt_1에 +1
            if cnt_1 == len_find - 1:   
                cnt += 1
            # cnt_1 과 len-find-1이 일치한다는 것은 find의 최초 글자 이후의 글자들이
            # 전부 일치한다는 뜻

    print('#{} {}'.format(tc, cnt))