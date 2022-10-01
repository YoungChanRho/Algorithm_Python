import sys
sys.stdin = open('input.txt','r')

T = int(input())

for tc in range(1,T+1):
    day, month, three_m, year = map(int,input().split())    # 정보 입력받기
    schedule = [0] + list(map(int,input().split()))
    dp = [0]*(13)    # 매달 수영장 이용 요금 정보가 담길 리스트

    for i in range(1,13):
        # 1일권, 한달권 비교
        dp[i] = min(day*schedule[i],month)+dp[i-1]
        if i >= 3:    # 3개월권 이용에 대한 정보도 포함 시켜야 할 경우
            dp[i] = min(dp[i],three_m + dp[i-3])
     
    
    ans = min(dp[12],year)    # 일년짜리 요금제를 사용할지, 아니면 3개월권과 한달권을 조합해서 사용할지
    print("#{} {}".format(tc, ans))


