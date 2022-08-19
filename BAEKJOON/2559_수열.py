N, K = map(int,input().split())     # N = len(lst)  K = 연속으로 측정하는 날의 수
arr = list(map(int,input().split()))        # 온도를 입력 받는다


start = sum(arr[:K])    # 처음에 더해주는 값들
lst = []                # 더한 값들이 담길 리스트
lst.append(start)       # 처음 더한 값을 일단 넣어 줌

for i in range(N-K):    # 앞에 숫자를 빼주고 뒤에 숫자를 더해 주는 식으로 숫자를 변경해 간다.
    start = start - arr[i]+arr[i+K]
    lst.append(start)

print(max(lst))



#----시간초과----#

# maxV = 0
# lst =[]
# for i in range(N-K+1):
#     sumV = 0
#     for j in range(K):
#         sumV += arr[i+j]
#     lst.append(sumV)
#     if lst[i] > maxV:
#         maxV = lst[i]

# print(maxV)


# maxV = 0
# for k in range(N-K+1):
#     if lst[k] > maxV:
#         maxV = lst[k]

# print(maxV)