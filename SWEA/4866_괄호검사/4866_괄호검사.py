# 4866_ 괄호검사
# 220818

# 우선 () {} 을 따로 뽑아서 리스트를 만들어준다.
# 그 이후로는 같은 방식으로 진행하면 될듯
# (,{, 가 들어오면 stack_list에 추가해주고
# 그 다음 경우로는
# ({) 경우는 그냥 0 출력
# 그리고 남아 있을 경우 즉 top이 -1이 아닌경우는 0


import sys
sys.stdin = open('sample_input.txt','r')

T = int(input())

for tc in range(1, T+1):
    row_arr = input()
    
    # 가로가 담긴 리스트
    arr = []
    # 각 방향의 가로만 담긴 리스트
    l = ['(','{']
    r = [')','}']

    # 먼저 (), {} 만 따로 모아둔 리스트를 만든다.
    for i in row_arr:
        if i == '(' or i ==')' or i =='{' or i =='}':
            arr.append(i)

    # 스택값이 담길 리스트
    stack_list = []
    top = -1
    answer = 0

    for i in arr:
        # top = -1 일 경우
        if top == -1:
            stack_list.append(i)
            top += 1
        # top != -1 인 경우
        else:
            # i가 (, { 인 경우
            # 일단 문제가 되지 않으니 넣어준다.
            if i in l:
                stack_list.append(i)
                top += 1
            # i가 ), } 인 경우
            else:
                # {}, () 일 경우
                if ((i == r[0] and stack_list[top] == l[0]) or 
                (i == r[1] and stack_list[top] == l[1])):
                    stack_list.pop()
                    top -= 1
                # 그 외의 경우는 {), (} 등과 같이 짝이 맞지 않는 경우를 의미한다.
                else:
                    answer = 0
                    break

    if top == -1:
        answer = 1
    else:
        answer = 0

    print('#{} {}'.format(tc, answer))
