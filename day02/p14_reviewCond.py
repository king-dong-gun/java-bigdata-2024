# file: p14_reviewCond.py
# desc: 리뷰02

# Q1
a = "Life is too short, you need python"

if "wife" in a :print('wife')
elif "python" in a and "you" not in a : print("python")
elif "shirt" not in a : print("shirt")
elif "need" in a : print("need")
else: print("none")

# Q2
result = 0
i = 1
while i <= 1000:
    if i % 3 == 0 :
        result += i
    i += 1
print(result)

# Q3
i = 0
while True:
    i += 1
    if i > 5 : break
    print('*' * i) 

# Q4
for i in range(1, 101) :
    print(i)

# Q5
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for score in A :
    total += score
average = total / len(A)
print('평균은', average)

# Q6
# 리스트 컴프리헨션 사용
numbers = [1, 2, 3, 4, 5]
result = [n * 2 for n in numbers if n % 2 == 1]
print(result)

# Q6과 같은 답
# numbers = [1, 2, 3, 4, 5]
# result = []
# for n in numbers == 1:
# if n % 2 == 1:
# result.append(n*2)