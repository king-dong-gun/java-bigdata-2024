# file: p22_carClass.py
# desc: 객체지향 클래스 학습

class Car :
    __carNum = '' # __ 변수 지정은 private
    carNum = '41러 8504' # 그냥 쓰면 public
    yourCar = '82마 5448'
    company = '삼성 '
    releaseYear = 2014
    color = '검정색'
    carType = '세단'
    fuelType = '가솔린'

    def __init__(self, carNum) -> None: # 생성자 -> None 리턴할게 없음
        self.__carNum = carNum
        print(f'{self.carNum} 객체를 생성합니다.')
        print('차 객체를 생성합니다.')

    def __str__(self) -> str: # 객체 변수를 print()할때 출력 커스터마이징 함수
        return f'내 차는 {self.company}, {self.carNum} 입니다!!'
    
    def getCarNum(self) :
        return self.carNum
  
    def getCarNum(self) :
        print(f'{self.carNum} 입니다.')

    def getCarColor(self) : 
        print(f'{self.carNum}는 {self.color} 입니다')

    def start(self) :
        print(f'{self.carNum}시동을 겁니다.')

    def accel(self) :
        print(f'{self.carNum}악셀을 밟습니다.')
    
    def brake(self) :
        print(f'{self.carNum}브레이크를 밟습니다.')

    def turnLeft(self) :
        print(f'{self.carNum}좌회전 합니다.')

    def turnRight(self) :
        print(f'{self.carNum}우회전 합니다.')

    def off(self) :
        print(f'{self.carNum}시동을 끕니다')