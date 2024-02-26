# file: d27_exeepctionHandel.py
# desc: 예외처리2
# 비정상적인 종료를 막기 위한 것

#while True :
#    try :
#        select = input('메뉴입력 1. 저장, 2. 검색, 3. 종료 >>')
#    except :
#        print('예외발생이 했습니다.')
#        continue

#    if select == 1 :
#        print('저장')
#    elif select == 2 :
#        print('검색')
#    elif select == 3 :
#        print('종료')
#        break
#    else :
#        continue


class Chicken :
    def fly(self) :
        raise NotADirectoryError
    
koko = Chicken()
try: 
    koko.fly()
except Exception as e :
    print('닭은 못날아요.', e.args)