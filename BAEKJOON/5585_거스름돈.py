K = int(input())    # 입력값
M = 1000 - K

lst = [500,100,50,10,5,1]
cnt = 0
for i in range(6):
    if M // lst[i]:
        cnt += M//lst[i]
        M = M -lst[i]*(M//lst[i])

print(cnt)