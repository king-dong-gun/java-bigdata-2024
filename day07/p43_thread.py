# file: p43_thread.py
# desc: 스레드 기본

# import threading
from threading import Thread, current_thread
import time

class BackgroundWorker(Thread) :
    def __init__(self, name) -> None :
        super().__init__(name=name)
        # self._name = f'{current_thread().getName()} : {name}' # DeprecationWarning 오류 -> 다음버전부터 없어진다는 경고
        self._name = f'{current_thread().name} : {name}' # getName 대신 name 사용

    def run(self) -> None:
        print(f'백그라운드워커 시작 : {self._name}')
        time.sleep(3)
        print(f'백그라운드워커 종료 : {self._name}')

print('메인 스레드 시작') # 메인엔트리에서 시작되는 프로세스 자신(메인 스레드)
for i in range(5) : 
    name = f'서브 스레드{i}'
    th = BackgroundWorker(name)
    th.start() # run 실행
    
print('메인 스레드 종료')