# k = 0

# A, B, V = map(int,input().split())

# while True:
#     if A*(k+1) - B*(k) >= V:
#         print(k)
#         break
#     else:
#         k += 1

# 달팽이는 V에 도달하면 멈추는데, A(k+1) -B(k)가 V보다 커지는 순간 답이 나온다.
# 먼저 내가 편한 방법으로 풀이를 해보고, 해당 방식으로 새로운 방법을 찾는 것도 방법인 듯.
# 시간 제한 문제를 해결하려면 반복문을 사용하지 말아야 한다.
A, B, V = map(int,input().split())

k=(V-B)/(A-B)

if k==int(k):
    print(int(k))
else:
    print(int(k)+1)
