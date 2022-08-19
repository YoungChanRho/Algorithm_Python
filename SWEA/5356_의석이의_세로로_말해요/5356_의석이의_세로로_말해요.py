# 5356_의석이의_세로로_말해요
# 220819

import sys
sys.stdin = open('input.txt','r')

T = int(input())

# 길이 구하는 함수
def lenVV(lst):
    lenV = 0
    for _ in lst:
        lenV += 1
    return lenV

for tc in range(1,T+1):
    arr = [list(input()) for _ in range(5)]     # 2차원 배열로 글자들을 입력받는다

    answer_list = [0]*75     # 정답이 담길 리스트
    for i in range(5):      # 행 바꿈을 해주기 위해
        for j in range(lenVV(arr[i])):   # 2차원 리스트 인덱스 접근을 위해 길이를 구해준다.
            answer_list[i+j*5] = arr[i][j]

    answer_list = [a_str for a_str in answer_list if a_str != 0]    # 0을 모두 제거해준다.

    answer_str = ''.join(answer_list)   # 리스트형태를 스트링형태로 ','을 모두 제거해서 출력한다.
                                        # '<어떤 걸로 항목들을 이어줄지>'.join()
    
    print('#{} {}'.format(tc, answer_str))

