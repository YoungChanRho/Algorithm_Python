# 입력을 받는다.
N, K = map(int,input().split())

# lst를 정수형으로 만들어준다
lst = [input() for _ in range(N)]
lst = list(map(int,lst))

coin_need = 0   # 필요한 동전의 개수
for i in range(N-1, -1, -1):    # lst의 큰 값부터 확인을 해준다.
    if (K // lst[i]):   # 만약 K//lst[i] 값이 0이 아니라면
        coin_need += K//lst[i]  # coin_need에 K//lst[i](나눴을 때의 몫)을 더해준다.
        K = K - lst[i]*(K//lst[i])  # 선택된 돈 만큼의 액수를 K값에서 빼준다.
        
print(coin_need)