# file: p25_Calculator.py
# desc: 클래스 리뷰

# Q1
class calculator :
    def __init__(self) -> None:
        self.value = 0

    def add (self, val) :
        self.value += 1

class upgradeCalculator(calculator) :
    def minus (self, val) :
        self.value -= 1


