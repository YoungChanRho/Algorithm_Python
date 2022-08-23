from curses.ascii import isdigit
import sys
sys.stdin = open('input.txt','r')

T = int(input())

for tc in range(1,T+1):

    tokens = input()    # 중위 계산법 식 입력받음
    ans = ''            # 후위 계산식이 담길 문자열
    stack = []          # 스택
    priority = {'*':3,'/':3,'+':2,'-':2,'(':1}  # 연산자간의 우선순위

    for n in range(len(tokens)):    # tokens문자열 길이 만큼 반복
        if tokens[n].isdigit():     # 만일 숫자라면
            ans.append(tokens[n])   # 바로 ans문자열에 삽입
        elif tokens[n] == '(':      # '('일 경우 스택에 삽입
            stack.append(tokens[n])
        elif tokens[n] == ')':      # ')'일 경우
            while stack[-1] != '(': # stack의 top값이 '('가 아니라면
                ans.append(stack.pop()) # stack에 pop을 하고, '('가 나올때까지 ans에 삽입
            stack.pop()             # '('이 나올 경우 pop
        else:   # stack의 top에 우선순위가 더 빠르거나 같은 것이 있을 경우
            while stack and priority[tokens[n]] <= priority[stack[-1]]:
                ans.append(stack.pop())
            stack.append(tokens[n])
    while len(stack) != 0:
        ans.append(stack.pop())

    ans = ''.join(ans)
    print(ans)