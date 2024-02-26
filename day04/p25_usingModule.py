# file: p25_usingModule.py
# desc: 모듈 사용

import calc # 나는 calc.py를 사용한다
# import calc as c   # calc를 c로 바꾸겠다
# from calc import multi   # multi() 라는 함수명만 사용한다
# from calc import multi as mul  # multi()를 mul()로 바꾸겠다

from Math import Math # from Math(모듈, 파일이름) import Math(클래스 이름)
# from day03 import p22_carClass # 디렉토리(모듈묶음:패키지).모듈


if __name__ == '__main__' : ## java의 void main()과 동일
# main 문 안에는 모두 tap 사용

    result = calc.add(10, 7)
    print('결과는', result)

    result = calc.multi(10, 7)
    print('결과는', result)


    print(__name__)  # __main__ = 나는 main엔트리다.

    myMath = Math()
    print(myMath.solve(10))
