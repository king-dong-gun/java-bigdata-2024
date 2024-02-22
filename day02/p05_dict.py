# file: p05_dict.py
# desc: 딕셔너리, 집합 자료형

# 딕셔너리 기본 모습
# dic = {Key1: Value1, Key2: Value2, Key3: Value3} # Key는 문자열을 자주 쓴다

spiderMan = {'name': 'Petter Parker', 'age': 18, 'weapon': 'Web shooter', 'freind': ["ironMan", 'Thor','Captain America']}
print(spiderMan)
print(spiderMan['name'])

# 딕셔너리 쌍 추가
spiderMan['job'] = 'CameraMan' # Key값 job 추가
print(spiderMan)

## 값 삭제
del spiderMan['freind'] # Key값 freind 삭제
print(spiderMan)  

## 딕셔너리 함수
print(spiderMan.keys()) # 딕셔너리에 현재 저장되어있는 Key 목록
# 직육면체 함수(뒤엔 무조건 ()나와야함), []직육면체 변수
print(list(spiderMan.keys())) # 키 목록을 리스트형태로 형변환(케스팅)
print(spiderMan.items()) # 모든 아이템 출력 (한키 마다 ()로 묶음)
print(spiderMan.get('job')) # 딕셔너리의 값 가져오기

print('freind' in spiderMan) # 딕셔너리안에 키가 있는지 확인

print(spiderMan.values()) # Key값들만 출력
res = spiderMan.pop('job') # 값을 꺼내오기
print(res)
print(spiderMan)
print(spiderMan.pop('age'))
print(spiderMan)

## 데이터만 삭제
spiderMan.clear()
print(spiderMan)

del spiderMan # 완전삭제
## print(spiderMan) #define 


## 집합
# 집합은 중복을 허용하지 않음, 순서가 없다.
# set[1,2,3,4,3,2,1] = 출력1: {1,2,3,4}, 출력2: {3,2,4,1} -> 순서 x, 중복 x
