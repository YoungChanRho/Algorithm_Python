N = int(input())
lst = list(map(int,input().split()))

# 감소
max_d = 0
d_cnt = 1
for i in range(1,N):
    if lst[i-1] >= lst[i]:
        d_cnt += 1
        if d_cnt >= max_d:
            max_d = d_cnt
    elif lst[i-1] < lst[i]:
        d_cnt = 1

# 증가
max_i = 0
i_cnt = 1
for i in range(1,N):
    if lst[i-1] <= lst[i]:
        i_cnt += 1
        if i_cnt >= max_i:
            max_i = i_cnt
    elif lst[i-1] > lst[i]:
        i_cnt = 1

if N==1:
    print(1)
elif max_i >= max_d:
    print(max_i)
else:
    print(max_d)

