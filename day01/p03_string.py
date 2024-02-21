# file: p03_string.py
# desc: 문자열 자료형과 연산

a = "Hello World"
print(a)
b = 'Hello World'
print(b)
c = "Hello, 'Ashley'"
print(c)
#탈출문자 \n 외 나머지는 파이썬에 잘 사용되지 않음

#문장을 여러줄로 쓰고 싶으면 \를 문장 끝에 붙힘
d = 'Hello~' \
'I\m Hugo' \
'Nice to meet you'
print(d)

#여려줄 문장 쓸때는
d = '''Hello~
    I'm Ashley.
    Nice to meet you'''
print(d)

##문자열 연산 + , *
before = 'I wanna go to'
after = 'Boracai~!'
print(before + after) # + -> 문자열을 합쳐서 하나의 문자열을 만들고 싶을때
print(after * 3)  # -> 한문자를 여러번 반복 나열하고 싶을때

##문자열 나열하기
print ('글자길이 =', len(before))
print('한글글자길이', len('안녕하세요'))

##문자열 인덱싱, 슬라이싱
cp = 'Life is too short, You need Python'  #DB 제외 모든 언어의 컴퓨터 수의 시작은 '0'
print(len(cp))

##슬라이싱
print(cp[8]) #cp의 8번째 문자 출력
print(cp[17]) #cp의 17번째 문자 출력

# print(cp[8]) = 'd'  문자열은 배열이지만 값을 변경하지 못함
print(cp [12 : 16+1]) # 문자열 범위 슬라이싱 -> : 뒤에 있는 숫자는 항상 +1 해준다

print(ascii('안'), ascii('녕'), ascii('하'), ascii('세'), ascii('요'))
print(chr(65))

# 기존 문자열로 새로운 문자열을 만들때는 슬라이싱, 다른 문자열로 대체 필수
print(cp [0 : 7], 'long', cp[17 : ]) # : 뒤의 수 생략하면 마지막 수까지
# 다른언어에는 없는 - 슬라이싱
print(c[-6])
print(cp [-11 : -7]) # -로 슬라이싱할때도 : 뒤의 수에 +1 해준다

## 문자열 포멧팅(format string)
## 파이썬에서는 %d, %s, %c 등 포멧스트링용 연산자 사용 빈도가 낮음
temp = 21
print('현재 온도는 %d도 입니다.' %temp)
temp = 17
print('현재 온도는 %d도 입니다.' %temp)

## format 함수로 포매팅 (가장 일반적)
print('현재 온도는 {0}도 입니다.' .format(temp))

## 날짜를 포맷으로 만들때
month = 2
day = 21
hour = 3
mins = 18
print('오늘은{0:02d}월 {1:02d}일 {2:02d}시 {3:02d}분 입니다.' .format(month, day, hour, mins))

#숫자 자료형
income = 6_000_000_000  #연매출
print('올해 매출액은 {0:,d}원' .format(income))
PI = 3.1415926536
print('파이는{0:10.2f}'.format(PI)) # 10.2f 소수점 . 까지 다 포함해서 10자리 수, 소수점은 2자리까지 출력
# print('{0}'.format(PI)) # 실수형은 d(정수형) 포매팅이 불가

## f포매팅 3.6(2016)버전 이후에 나온 최신 방식 
name = '홍길동'
age = 30

cont = f'나는 {name}이고, 나이는 {age} 입니다.'
print(cont)
name = '김동건'
age = 20
cont = f'나는 {name}이고, 나이는 {age} 입니다.'
print(cont)
print(f'나는 {name:>10}이고, 나이는 {age:03d}세 입니다.') # name 앞 10자리 띄어쓰기
print(f'나는 {name:<10}이고, 나이는 {age:03.1f}세 입니다.') # name 뒤 10자리 띄어쓰기
# 정수는 f포맷 사용가능, 실수는 d포맷 사용불가

## 문자열 함수
a ='Life is short, You need Python'

print(a.count('Life')) # 문자 life의 수 찾기
print(a.count('o')) # 문자 o의 수 찾기

print(a.find('sh')) # 문자열 중 첫번째 sh 위치 찾기

print(a.index('t')) # 문자열 중 첫번째 t의 위치 찾기
#print(a.index('k')) # index()는 count()로 갯수가 0이 아닐때만 호출, k가 없으므로 오류발생
print(','.join('abcde')) # a,b,c,d,e

print(a.upper()) # 모든 문자열을 대문자로 변경
print(a.lower()) # 모든 문자열을 소문자로 변경
print(a.capitalize()) # 문장이 시작되는 첫번째 문자만 대문자로 변경

origin = '          H   i          '
print(f'++{origin}++')
print(f'++{origin.lstrip()}++') # 왼쪽 공백 없앰 lstrip
print(f'++{origin.rstrip()}++') # 오른쪽 공백 없앰 rstrip
print(f'++{origin.strip()}++') # 양쪽 공백 없앰 strip

print(cp.replace('too','').replace('short', 'long')) # 문자열 바꾸기

## 문자열 자르기 -> 리스트(파이썬은 배열이 없음)
cpWords = cp.split() # 문자열 나누기
print(cpWords)