A, B = map(int,input().split())

if A>B:
    print('>')
elif B<A:
    print('<')
else:
    print('==')

score = int(input())
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')