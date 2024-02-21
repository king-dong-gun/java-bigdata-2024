# file: p02_number.py
# desc: 숫자형 자료타입 및 연산

age = 40 # int형 수자를 담는 변수

taxRate = 8.8 #float형 실수를 담는 변수

highFloats = 4.24E10 #지수승(float)

print('나이는', age) # 문자열이 "" , '' 둘다 사용 가능함
print('세율은', taxRate)
print('지수값', highFloats)


#특수 수자형
binVal = 0b11111111 # = 255 (컴퓨터 때문에 만든 수)
octVal = 0o11 #9 1~7 10(8)         ~~
hexVal = 0xFF #255 0~9ABCDEF(컴퓨터 때문에 만든 수)
print('2진수', binVal, '8진수', octVal, '16진수', hexVal)

#결론: 타입을 적을 필요가 없음

a, b, c = 3, 4, 5
print (a + b)
print ( a - c)
print (a * c)
#단, 나누기( / )는 3가지로 분류함
print (c / b)  #정확하게 나누기
print (c // b) #정수로만 나누기 (나머지 들어오지 않음, java로 int형)
print (c % b)  #정수로 나눈 나머지 (나머지만 출력)

print (2 ** 10) #1024 import math; math pow() -> 2^10 

print ((a + b) * c) #연산자 우선순위는 다 필요없고, ()만 잘 쓰면 끝
