# file : p04_list.py
# desc : 리스트

## 파이썬에는 배열이 없다. 리스트로 대신함
even = [2,4,6,8,10]
odd = [1,3,5,7,9]

print(even)
print(even[4]) # 길이가 n일때 마지막 인덱스는 n-1

even[4] = 20
print(even) # 리스트는 인덱스의 값을 변경가능

datas = [123, 45.6, True, 'Hello', odd, None] # 형지정 없기 때문에 어떤 자료형이든 다 리스트에 할당가능
print(datas) # 6개의 배열, 6 - 1 출력

## 인덱싱, 슬라이싱
print(odd[2])
print(even[0] + odd[0])

cpWord = ['Life', 'is', 'short']
print(cpWord[0]+ cpWord[2])

print(even[1:3+1])


## 2차원 리스트
# 3행 4열
# [[1,2,3,4] ,
# [5,6,7,8],
# [9,10,11,12]]

d2Datas = [[1,2,3,4],
           [5,6,7,8],
           [9,10,11,12]]

for i in d2Datas :
    print(i)
    
dm1col1 = [1,2,3,4]
dm1col2 = [5,6,7,8]
dm1col3 = [9,10,11,12]
print([dm1col1, dm1col2, dm1col3])

# 리스트 연산은 문자열 연산과 동일
print(even + odd)
print(odd * 2)

## 값 변경
even[3] = 10 # even 배열의 n-1번 숫자 변경
print(even)

del even[2] # even 배열의 n-1번 삭제
print(even)

## 리스트 관련 함수

# append 리스트 제일 뒤에 추가
even.append(30) # 리스트 제일 뒤에 30 추가
print(even)

# insert 원하는 위치 값 추가
even.insert(2, 6) # 인덱스 2에다가 6 추가
print(even)

# 정렬 -> 리스트를 거의 쓰는 이유
origin = [45, 23, 9, 17, 1, 5, 11, 3, 29, 30] # 리스트의 요소가 뒤죽박죽 있는걸 순서대로 정렬해줌
origin.sort()
print(origin)
origin.sort(reverse=True) # 내림차순(Descending)
print(origin)

# 뒤집기
aa = ['a', 'f' , 'e', 'b'] # 내림차순과 다름 리스트 순서를 뒤집는 것
aa.reverse()
print(aa)

print(aa.count('a'))
print(aa.index('e'))

bb = [1, 3, 5, 6, 8, 3, 1]
bb.remove(3) # 맨 처음 정의된 3만 제거, 2번째 3은 남음
print(bb)

print(even.pop()) # 마지막 값을 끄집어 냄
print(even.pop()) # 스택의 기능 append()는 마지막에 할당해줌 <-> pop()은 마지막 값 끄집어 냄
print(even) # pop으로 20, 30을 끄집어 냈기 때문에 2,4,6,10만 출력

## 튜플
# 리스트 = 튜플(동일), 단 삭제or변경 불가능
tVal = (1, 3, 5, 7, 9)
# tVal[2] = 1  리스트는 가능, # 튜플은 한번 만들어지면 끝까지 사용해야함
# del tVal[2]  리스트는 가능, # 튜플은 한번 만들어지면 끝까지 사용해야함