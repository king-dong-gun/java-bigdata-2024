# file: p23_carSample.py
# desc: Car 클래스 사용해보기

from p22_carClass import Car

myCar = Car('41러 8504') # 클래스를 사용해서 객체 하나를 생성
yourCar = Car('82마 5448')

# print(myCar)
# print(yourCar)
myCar.carNum = 'SM5'
myCar.company = '삼성'
myCar.carType = '세단'
myCar.fuelType = '가솔린'
myCar.releaseYear = '2014'
print(myCar)

myCar.getCarColor()
myCar.start()
yourCar.start()
myCar.accel()
myCar.turnLeft()
myCar.turnRight()
myCar.brake()

