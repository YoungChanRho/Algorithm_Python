# 고정비용: A / 가변비용: B
# ex. A=1000 , B=70
# 한대 생산 비용 1070
# 열대 생산 비용 1000 + 10*70 = 1070
# 노트북 가격: C
# 총 수입(판매 )

A, B, C = map(int,input().split())
if C <= B:
    print(-1)
else:
    N = (A//(C-B))+1
    print(N)