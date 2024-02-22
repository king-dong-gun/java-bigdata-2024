# file: p09_ifcond.py
# desc: if 제어문

money = 1800

if money >= 5000:
    # indentation(들여쓰기) tab == space 4번
    print('택시타고 가')
    print('부럽네')
elif money<5000 and money>= 2500:
    print('기사님 저 앞까지만 가주세요')
    print('집까지 걸어감')
else:
    print('걸어가~')
    print('돈도 없는게...')

    a, b, c, d = 10, 5, 7, 9
    print(a >= b) # True
    print(c > d) # False

    print(a >= b and c > d) # False 1 and 1 == 1 / 1 and 0 == 0 / 0 and 0 == 0
    print(a >= b or c > d) # True 1 or 1 ==1 / 1 or 0 ==0 / 0 or 1 == 0 / 0 or 0 == 0
    # 실무 비율 and 80%, or 20%
    print(not(a >= b)) # False
    
    ## print() end=(많이 씀), sep= 옵션있음
    print(1 in [1, 3, 5, 7, 9], end=', ') # 1이 배열에 속해 있느냐 True 
    print(6 in [1, 3, 5, 7, 9]) # 6이 배열에 속해 있느냐 False
    # 한줄로 표현하고 싶을때 end=
    print('13579', '246810', sep='||') # sep= 문자열 사이에 문자 넣기




