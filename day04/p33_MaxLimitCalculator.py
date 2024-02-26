# file: p33_MaxLimitCalculator.py
# desc: Calculator 클래스 문제


from p32_Calculator import MaxLimitCalculator

cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)

print(cal.value)

# Q6
# 리스트 항목마다 3을 곱하여 리턴하기
def ttime(x) :
    return x * 3
print(list(map(ttime, [1,2,3,4])))

# Q7
# 최댓값과 최솟값의 합
x = max([-8, 2, 7, 5, -3, 5, 0, 1])
y = min([-8, 2, 7, 5, -3, 5, 0, 1])
print(x + y)

# Q8
# 소수점 반올림하기
print(round(5.666666666667, 4))

# Q11
# 날짜 표시하기
import datetime

curr = datetime.datetime.now()
print(f'{curr.year}/{curr.month:02d}/{curr.day}  {curr.hour}:{curr.minute:02d}:{curr.second}')

# Q12
# 로또 번호 생성하기

import random

total = []
result = []

for i in range(5) :
    while True :
        val = random.randint(1, 45)
        while val not in result :
            result.append(val)
        if len(result) == 6 :
            break
    result.sort()
    total.append(result)
    result = []
print(total)

# Q13
# 생일 차이 구하기

import datetime
sister = datetime.date(1995, 11, 20)
brother = datetime.date(1998, 10, 6)
diff = brother - sister
print(diff)





