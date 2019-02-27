# %f: 모든 소수점 출력
# %.2f : 소수점 두자리까지 출력

# 0개의 수를 입력 받아, 최대 수와 최소 수를 제외한 나머지의 평균값을 출력하는 프로그램을 작성하라.
# (소수점 첫째 자리에서 반올림한 정수를 출력한다.)

import sys
sys.stdin = open('1984 중간 평균값 구하기.txt','r')


T = int(input())
for tc in range(1,T+1):
    nums = list(map(int,input().split()))

    #최대수 최소수 구하기
    max_num = nums[0]
    min_num = nums[0]

    for num in nums:
        if num> max_num:
            max_num = num
        if num< min_num:
            min_num = num
    #최대수 최소수 제외
    nums.remove(max_num)
    nums.remove(min_num)

    #평균을 위한 리스트 합
    s = 0
    for num in nums:
        s += num

    # 평균
    # 소수점 첫째 자리에서 반올림한 정수
    #avg = ('%.01f' % (s/len(nums)))
    avg = round(s / len(nums))
    print(f"#{tc} {avg}")
