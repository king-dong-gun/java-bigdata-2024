# file: p15_function.py
#desc: 함수 학습

def plus(a, b) : # 매개변수 + 리턴값
    res = a + b
    return res

def minus(a, b): # 매개변수, 리턴값x
    res = a - b
    print(res)

def mutiple(): # 매개변수x, 리턴값o
    res = a * c # 밖에 있는 전역변수 a,c 를 사용하겠다
    return res

def divide() :
    global a,c 
    print(a / c)

def pow(a = 2, b = 10) : # 기본인수를 지정할때는 뒤에서부터
    res = a ** b
    return res

print('더하기')
a = 10
c = 7
result = plus(a, c)
print(result)

minus(a, c)
result = mutiple()
print(result)
divide()

print(pow()) # 기본 인수 -> 2^10

def plus_many(*items): # 입력값이 많을때 (*매개변수): , 동적 매개변수
    result = 0
    for item in items:
        result += item

    return result
print(plus_many(1,2))
print(plus_many(1,2,3))
print(plus_many(1,2,3,4,5))
print(plus_many(1,2,3,4,5,6,7,8,9,10))

def calcurator(mode, *args):
    if mode == 'a':  # 더하기
        result = 0
        for i in args:
            result += i
    elif mode == 'm':  # 빼기
        result = args[0]
        for i in args[1:]:
            result -= i
    elif mode == 'mult':  # 곱하기
        result = 1
        for i in args:
            result *= i
    elif mode == 'd':  # 나누기
        result = args[0]
        for i in args[1:]:
            result /= i

    return result

print(calcurator('a', 1, 2, 3, 4, 5))
print(calcurator('m', 100, 10, 5, 4))
print(calcurator('mult', 2, 2, 2, 2, 2))
print(calcurator('d', 100, 5, 4))

def print_kwargs(**items) :
    print(items)

print_kwargs(name = 'Peter parker', age = 18, weapon = 'web shooter')

# 리턴을 한번에 여러개 (두개 이상)할 수 있다. 튜플로 리턴
def calcurator2(a, b) :
    res1 = a + b
    res2 = a - b
    res3 = a * b
    res4 = a / b
    return res1, res2, res3, res4

a, b, c, d = calcurator2(3, 4)

print(a, b, c, d)

# 람다식(익명 함수)
add = lambda a, b: a + b # 람다함수 끝, 람다식은 두개의 인수를 가짐
print(add(5,4))





