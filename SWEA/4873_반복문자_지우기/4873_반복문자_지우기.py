import sys
sys.stdin = open('sample_input.txt','r')

T = int(input())


# 한 글자만 남아있을 때 

for tc in range(1, T+1):

    arr = input()
    # 처음 값을 담아둔 상태
    stack_list = []
    top = -1

    # arr의 길이
    len_arr = 0
    for _ in arr:
        len_arr += 1

    # arr의 길이만큼 반복
    for i in range(len_arr):

        # 비어있다는 것을 의미하기 때문에, 값을 채워주고 top을 올려준다.
        if top == -1:
            stack_list.append(arr[i])
            top += 1            
        
        # 2. 들어오는 값이 stack_list[top]값과 다를 경우
        # 새로운 값을 추가해주고 top += 1을 진행           
        else:
            if arr[i] != stack_list[top]:
                stack_list.append(arr[i])
                top += 1

        # 3. 들어오는 값이 stack_list[top]값과 같을 경우
        # 되도록 if / else 를 사용하기
            else:
                stack_list.pop()
                top -= 1
        
    if top == -1:
        anser = 0
    else:
        answer = top + 1

    print('#{} {}'.format(tc,answer))







    # for i in range(1,len_arr):
    #     # 만약 top에 들어있는 값과 새로 들어올 값이 다르다면
    #     if top == -1:
    #         stack_list.append(arr[i])
    #         top += 1
    #     if arr[i] != stack_list[top]:
    #         top += 1
    #         stack_list.append(arr[i])
    #     # 만약 top에 들어있는 값과 들어오는 값이 같다면
    #     # top값 삭제해주고,top -= 1 진행
    #     elif arr[i] == stack_list[top]:
    #         stack_list.pop(top)
    #         top -= 1

            


