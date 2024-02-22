# file: p12_gugudan.py
# desc: 구구단 프로그램

# 일반 for문 
#x = 2 
#for i in range(1, 10) : # 1~9까지
#        print(f"{x} × {i} = {x*i}")

#x = 3
#for i in range(1, 10) : # 1~9까지
#        print(f"{x} × {i} = {x*i}")

# 2중 for문
print('***구구단 프로그램***')
for i in range(2, 10) :
    print(f'{i}단 시작 =======>')
    for j in range(1, 10) :
        print(f'{i} x {j} = {i*j:2d}',end='\t')
    print() # 아무런 내용없이 \n 해줘 (println)
        