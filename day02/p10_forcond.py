# file: p10_forcond.py
# desc: for 반복문

# for item in 반복할 객체or변수명 :
#   ...

a = [1, 3, 5, 7, 9]
print(type(a)) # <class 'list'>

for i in ['one', 'two', 'three']:
    print(type(i))

b = [(1, 2), (3, 4), (5, 6)] # tuple의 리스트
for i in b:
    print(i)

for (first, second) in b: # 튜플의 ()는 생략 가능
    print(first, second)

# 평균 구하기
grade = [90, 80, 50, 70, 10]
sum = 0

for i in grade :
    sum += i
    print(sum) # 총합
    print(sum / len(grade)) # 평균

    # range()
    print(range(10))
    print(range(0,10))

    for i in range(0, 10) : 
        print(i, end=', ') # 0~9까지의 범위
    print()

    print(list(range(0,10)))  # 리스트 표현식

    print(list(range(0, 10+1, 2))) # 0부터 짝수만 올라옴
    print(list(range(1, 10, 2))) # 0부터 홀수만 올라옴

    print(list(range(10, 0, -2)))
    print(list(range(4, 101, 4)))
    print(list(range(10, 0, -1)))

    res = 0
    for i in range(1, 11) :
        res += i
        print(res)

## list comprehension \ 리스트 내포
    # list(range())만으로도 리스트를 생성할 수 있지만, 여러조건으로 리스트 생성할때는 컴프리헨션이 간편함
        print([i for i in range(1, 1001)])

        print(([num * 3 for num in range(1, 1001) if num % 3 == 0]))

    result = [x * y for x in range(2, 10)
                    for y in range(1, 10)]
    print(result)