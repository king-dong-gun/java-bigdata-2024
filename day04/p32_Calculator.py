# file: p32_Calculator.py
# desc: 클래스 상속 리뷰

class Calculator :
    def __init__ (self) :
        self.value = 0
    def add (self, val) :
        self.value += val

class MaxLimitCalculator(Calculator) :
    def add(self, val) :
        self.value += val
        if self.value > 100 :
            self.value = 100

