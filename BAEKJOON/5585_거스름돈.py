K = int(input())    # 입력값
M = 1000 - K

# 거스름돈을 lst속의 가장 큰 값으로 순차적으로 나눠주고, 나눈 몫과 나눠준 값을 곱한 값을 계속 빼는 식으로 진행

lst = [500,100,50,10,5,1]
cnt = 0
for i in range(6):
    if M // lst[i]:
        cnt += M//lst[i]
        M = M -lst[i]*(M//lst[i])

print(cnt)