# 4874_forth
# 220823
from distutils.log import error
import sys
sys.stdin = open('input.txt','r')


def calculate(expression):  # 계산 하는 함수 정의
    stack = []  # 빈 스택
    idx = 0     # expression 리스트의 인덱스 값, 인덱스를 변화시키면서 스택에 담아줄 것이기 때문에
    math_operator = ['+','-','/','*']   # 연산자 목록
    while True:
        if expression[idx] =='.':   # '.' 를 만날 경우
            if len(stack) != 1:     # '.'가 나올 경우, stack에는 숫자가 하나만 있어야 한다.
                ans = 'error'
                break
            else:
                ans = stack.pop()   # 마지막 숫자를 pop해주고 ans에 담아준다
                break
        elif expression[idx] not in math_operator:  # 숫자를 꺼낼 경우
            stack.append(int(expression[idx]))      # 숫자를 정수로 변환하고 stack에 담아준다.
            idx += 1                                # 인덱스값 증가하여 리스트의 다음 요소에 접근한다.
            continue
        elif expression[idx] in math_operator:   # 연산자를 꺼낼 경우
            if len(stack) <= 1:                  # 연산자를 꺼냈는데 stack에 숫자가 2개보다 적을 경우, 'error'
                ans = 'error'
                break
            else:   # stack에 요소가 2개 이상 있을 경우
                first_pop_num = int(stack.pop())     # 첫번째 pop
                second_pop_num = int(stack.pop())    # 두번째 pop
                if expression[idx] == '+':
                    stack.append(second_pop_num + first_pop_num)
                    idx += 1
                elif expression[idx] == '-':
                    stack.append(second_pop_num - first_pop_num)
                    idx += 1
                elif expression[idx] == '*':
                    stack.append(second_pop_num * first_pop_num)
                    idx += 1
                elif expression[idx]== '/':
                    stack.append(second_pop_num // first_pop_num)
                    idx += 1
                    
    return ans

T = int(input())
for tc in range(1,T+1):
    expression = input().split()    # 리스트 형태로 문자들을 따로 저장
    print('#{} {}'.format(tc,calculate(expression)))
