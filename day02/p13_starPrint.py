# file: p13_starPrint.py
# desc: 별찍기

print('예제 그림')
for i in range(1, 6) :
    print('*' * i)

## 2중 for문으로 결과 만들기
print('\n')

print('별 찍기 --->>')
for i in range(1, 6) : # 첫 번째 반복문(for i in range(1, 6))은 역삼각형의 줄 수를 결정
    for j in range(i, 6) : # 두 번째 반복문(for j in range(i, 6))은 각 줄마다 공백을 출력
        print(' ', end='')

    for j in range(6-i, 6) : # 세 번째 반복문(for j in range(6 - i, 6))은 각 줄마다 해당 줄의 위치부터 끝까지 별표를 출력
        print('*',end='')
    print()