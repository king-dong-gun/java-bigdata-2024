# file: p21_review03.py
# desc: 문제
 
# Q1
def is_odd(number) :
    if number % 2 == 1 :
        return True
    else :
        return False
print(is_odd(3))
print(is_odd(4))

# Q2
def avg_numbers(*args) :
    result = 0
    for i in args :
        result += i
    return result / len(args)
print(avg_numbers(1,2))
print(avg_numbers(1,2,3,4,5))

# Q3
input1 = input('첫번째 숫자를 입력하세요: ')
input2 = input('두번째 숫자를 입력하세요: ')

total = int (input1) + int (input2) # 문자열이 연결되기 때문에 int형으로 케스팅해서 출력
print('두 수의 합은 %s 입니다.' % total)




# Q7
f = open('./day03/test.txt', 'w')
f.write ('Life is too short\n')
f.write ('you need java\n')

## readlines() 쓸때
f = open('./day03/test.txt', mode='r', encoding='utf-8')
body = f.readlines() # 결과가 list로 리턴
f.close()

body = [body[0], body[1].replace('java', 'python')]

# print(body)

body = [line.replace('java', 'python')for line in body]
f = open('./day03/test.txt', 'w', encoding='utf-8')
f.write(body[0] + body[1])
f.close()

## read() 쓸때

f = open('./day03/test.txt', mode='r', encoding='utf-8')
body = f.read() # 문자열로 리턴, 하지만 read()는 텍스트가 길면 문장이 잘려나온다
f.close()

body = body.replace('java', 'python')
f = open('./day03/test.txt', mode= 'w', encoding='utf-8')
f.write(body)
f.close()

