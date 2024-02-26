# file: p26_execptionHandle.py
# desc: 예외처리
# 오류(Error): 코드상 빨강,노란색의 밑줄이 그어지는 것
# 예외(Exception): 프로그램 실행중에 생기는 오류(비정상적 종료)

try :
    f = open('./sanple.txt', mode='r', encoding='utf-8') # -> f = open('없는 파일', 'r')
## ~~~~
    res = f.readline()
    print(res)
except :
    print('파일오픈 예외발생')
else : # 오류가 없는 경우에만 수행
    f.close()
#finally :
    #try : # try ~~ except는 다중으로 사용하면 성능에 별로 좋지 않다
    #f.close()   # 예외가 발생했든 안했든 무조건 파일 close() 필수!!
    #                # f에 파일 객체자체가 없어서 close() 불가
    #except NameError :
    #   print('파일오픈 실패')

try :
    print(5/0) # -> 0으로 나누려고 하면 오류
except ZeroDivisionError as e:
    print('나누기 예외발생', e.args)

#a, b = 5, 3
#if a == b :
    #print(True)