# file: p29_builtinFunc.py
# desc: 내장함수

## abs(absolute) 절대값
print(abs(-5))

## all  현재 컬랙션(반복 가능한 값[리스트,집합])의 데이터 조건이나 값이 참인 값만 있는지 확인
print(all([1,2,3,4,2,5]))

## chr() 아스키나 유니코드 값을 받아서 글자로 변경
print(chr(97)) # 아스키
print(chr(44032)) # 유니코드

## ascii() 영문자, 문자를 아스키숫자와 유니코드숫자로 변경
print(ascii('가'))

## dir() 객체가 지닌 변수, 함수를 알려주는 함수
print(dir(list()))
print(dir(dict()))

## divmod는 나눈 값을 몫과 나머지를 튜플로 리턴
print(divmod(10,3))

## *** enumerate() 열거하다라는 뜻 ***, 데이터 포함해서 인덱스를 같이 생성해주는 역할
for i in ['Hello', 'World', 'Python'] :
    print(i)

for i, data in enumerate(['Hello', 'World', 'Python']) :
    print(f'{i}번째 값은 {data} 입니다.')

## eval(evaluate) 실행함수 -> 문자열로 된 수식, 함수를 실행해주는 역할
print(eval('divmod(10,3)'))

## hex는 10진수를 16진수로 바꿔주는 역할
print(hex(255)) # 0xff

## map은 여러값을 한꺼번에 같은 조건으로 변경할 때
def ttime(x) :
    return x*2

print(list(map(ttime, [1, 3, 5, 7, 9]))) # map을 써서 반복데이터를 ttime함수로 처리
print(list(map(int, [1.0, 2.0, 3.0, 4.4]))) # map을 써서 반복데이터를 int로 처리

## max(), min()
print(max([3, 9, 99]))
print(min([3, 9, 99]))

## oct() 8진수
print(oct(34))

## ord() = ascii()
print(ord('A'))
print(ord('가'))

## round() 반올림
print(round(4.3, 0))

# sum() 반복되는 컬렉션 자료
print(sum(range(1, 101)))

## tuple() 다른 컬랙션을 튜플 자료형으로 변경
print(tuple([1, 2, 3, 4, 5]))

## *** type() *** 변수, 데이터의 타입 리턴
print(type('Hello')) # <class 'str'>
aa = [1, 2, 3, 4]
print(type(aa)) # <class 'list'>

## zip() 동일한 개수로 데이터를 묶어서 리턴
odd = [1, 3, 5, 7, 9]
even = [2, 4, 6, 8, 10] # 인덱스 갯수가 일치하지 않으면 일치하는 인덱스까지만 묶음, 나머지는 버림
norm = [1, 2, 3, 4, 5]

total = list(zip(odd, even, norm))
print(total)