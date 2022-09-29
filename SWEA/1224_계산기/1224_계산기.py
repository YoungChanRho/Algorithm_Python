import sys
sys.stdin = open('input.txt', 'r')

def my_postfix(expression):
    stack = []
    ans = ''
    priority = {'*':3,'+':2,'(':1}

    for i in range(len(expression)):
        if expression[i].isdigit(): # 숫자라면
            ans += expression[i]    # ans문자열에 삽입
        elif expression[i] == '(':  # '('가 나온다면 (근데 우선순위가 높은 연산자가 위에 들어올 때는 어떻게 처리 되는 것인가)
            stack.append(expression[i]) # stack에 추가
        elif expression[i] == ')':  # 닫힌 괄호가 나올 경우, 열린 괄호가 나올때까지 pop을 계속 진행
            while stack[-1] != '(':
                ans += stack.pop()  # stack[-1] == '(' 일 경우, while문을 탈출한다.
            stack.pop() # 그리고 stack[-1], 즉 열린 괄호를 pop해준다.
        else:   # 연산자가 나올 경우
            while stack and priority[expression[i]] <= priority[stack[-1]]: # stack이 차 있고, stack[-1]에 들어있는 연산자 우선순위가 새로 들어오는 연산자 보다 높다면
                ans += stack.pop()
            stack.append(expression[i])
    while len(stack) != 0:
        ans += stack.pop()
    return ans

def my_calculate(postfix_lst):
    stack = []      # 피 연산자를 담아줄 공간
    # ans_calculate = ''      # 최종 계산 값이 담길 곳 (굳이 필요한가 ?)
    
    for i in range(len(postfix_lst)):       # 후위 표현식 길이 만큼 반복문을 진행
        if postfix_lst[i].isdigit():    # 숫자일 경우
            stack.append(postfix_lst[i])
        else:   # 연산자를 만날 경우, 따로 우선순위를 고려해 줄 필요 x 
            if postfix_lst[i] == '+':   
                second_num = int(stack.pop())
                first_num = int(stack.pop())
                stack.append(first_num + second_num)
            elif postfix_lst[i] == '*':
                second_num = int(stack.pop())
                first_num = int(stack.pop())
                stack.append(first_num * second_num)
    return stack.pop()


for tc in range(1, 11):
    len_expression = int(input())
    expression = input()

    postfix_lst = my_postfix(expression)
    print(my_calculate(postfix_lst))



    
