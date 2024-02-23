# file: p24_ionic.py
# desc: 클래스 상속

from p22_carClass import Car

class Ionic(Car) : # Car 클래스를 상속 받아서 ionic을 만듬
    __fuelRate = 0.0 # 연비

    def setfuelRate(self, rate) :
        self.__fuelRate = rate

    def getfuelRate(self) -> float :
        return self.__fuelRate
    
    def getCarNum(self) -> str : # 함수 오버라이딩 (메소드 재정의)
        return (f'소중한 제 차는 {super().carNum} 입니다.')
    

myCar = Ionic('41러 8504')
myCar.company = "기아자동차"
myCar.setfuelRate(11)
print(myCar)
print(f'내차의 연비는 {myCar.getfuelRate()}km/1 입니다')
print(myCar.getCarNum())
