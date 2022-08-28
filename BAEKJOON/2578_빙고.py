import sys
sys.stdin = open('input.txt','r')

arr = [list(map(int,input().split())) for _ in range(5)]    # 내 빙고판
ans = [list(map(int,input().split())) for _ in range(5)]    # 사회자 정답

def horizon_sum(arr):
    cnt = 0
    for i in range(5):
            if sum(arr[i]) == 0:
                cnt += 1
    return cnt

def vertical_sum(arr):
    cnt = 0
    for i in range(5):
        sum_vertical = 0
        for j in range(5):
            sum_vertical += arr[j][i]
        if sum_vertical == 0:
            cnt += 1
    return cnt

def right_up_sum(arr):
    cnt = 0
    sum_right_up = 0
    for i in range(5):
        sum_right_up += arr[4-i][i]
    if sum_right_up == 0:
        cnt += 1
    return cnt

def left_up_sum(arr):
    cnt = 0
    sum_left_up = 0
    for i in range(5):
        sum_left_up += arr[i][i]
    if sum_left_up == 0:
        cnt += 1
    return cnt

new_ans_lst = []    # 사회자 정답 리스트
for i in range(5):
    for j in range(5):
        new_ans_lst.append(ans[i][j])


flag = True
call_cnt = 0
for i in range(25):
    call_cnt += 1
    for j in range(5):
        for k in range(5):
            if new_ans_lst[i] == arr[j][k]:
                arr[j][k] = 0
                if (vertical_sum(arr) + horizon_sum(arr) + left_up_sum(arr) + right_up_sum(arr) >= 3):
                    flag = False
                    break
        if(flag==False):
            break
    if(flag==False):
        break

                    
print(call_cnt)