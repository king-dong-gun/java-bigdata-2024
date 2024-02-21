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
print(datas)