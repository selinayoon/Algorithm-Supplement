# 월은 1 이상 12 이하의 정수이다. 각 달의 마지막 날짜는 다음과 같다.
# 1/31, 2/28, 3/31, 4/30, 5/31, 6/30, 7/31, 8/31, 9/30, 10/31, 11/30, 12/31
# 두 번째 날짜가 첫 번째 날짜보다 항상 크게 주어진다.

# 같은 달인 경우
# d1:1~ d2:10 => 10-1+1

# 다른 달인 경우
# d1:3/30 ~ d2:4/2 => 4월은 기준일d2 - 첫일 (2-1+1) => 3월 말일~기준일d1(31-30+1)

# 두 날 사이 온전한 달이 있을 경우
# d1: 3/30 ~ d2:5/5 =>4월이 온전히 들어가있음 => 편리하게 딕셔너리or 리스트를 사용한다.
import sys
sys.stdin = open('1948 날짜 계산기.txt','r')
T = int(input())
for tc in range(1,T+1):

    m1,d1,m2,d2 = map(int,input().split())


    month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    if m1 == m2:
        result = d2 -d1 +1
    else:
        mon = 0
        for ms in range(m1+1,m2):
            mon += month[ms]
        result = mon + d2+ (month[m1] - d1+1)


    print(result)