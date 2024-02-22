# file: p06_bool.py
# desc: 불타입 학습

# bool(참, 거짓) Java에선 boolean

a = True # True, False는 앞글자 무조건 대문자
b = False
print(a)
print(type(a)) # <class 'bool'>
print(type(1)) # <class 'int'>
print(type(3.14)) # <class 'float'>
print(type('Hello')) # <class 'str'>
print(type([1,2,3])) # <class 'list'> 
print(type((1,2,3))) # <class 'tuple'>

print(a == b) # 참
print(a == (not b)) # 거짓

print(bool('H'))
# 참/거짓 구분 (빈값,0,None False 그 외는 True)

# None 타입
C = None
# C가 정의 되지 않았습니다.
print(C)
print(a + b) # a True(1) False(0)

C = 3
print(C + a)