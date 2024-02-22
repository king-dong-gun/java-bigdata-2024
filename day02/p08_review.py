# file: p08_review.py
# desc: 리뷰

# Q1
korean = 80
english = 75
math = 55
print("평균: ", (korean + english + math) / 3)

# Q2
a = 13
print('a는 ', end='')
if a % 1 :
    print('짝수')
else :
    print('홀수')

# Q3
pin = '881120-1068234'
# 문자열 슬라이싱
yyyymmdd = pin.split('-')[0]
num = pin.split('-')[1]
print(yyyymmdd)
print(num)
# print('yyyymmdd: ', pin[0 : 5])
# print('num: ', pin[7 : 12])

# Q4
pin = '881120-1068234'
print('성별을 가르치는 숫자: ', pin[7])

# Q5
a = "a:b:c:d"
b= a.replace(':', '#')
print(b)


# Q6
a = [1, 3, 5, 4, 2]
a.sort()
print(a)
a.sort(reverse=True)
print(a)

# Q7
a = ['Life', 'is', 'too', 'short']
result = " ".join(['Life', 'is', 'too', 'short'])
print(result)

# Q8
a = (1, 2, 3)
a = a + (4,)
print(a)

# Q10
a= {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(a) # {'A':90, "C": 70}
print(result)

# Q11
a = [1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5]
aSet = set(a)
b = aSet
print(b)







