# file: p18_fileRead.py
# desc: 텍스트 파일 읽기

f = open('./day03/sample.txt', mode='r', encoding='utf-8')
f2 = open('./day03/dest.txt', mode='w', encoding='utf-8')  # 텍스트 파일 Copy
###
read = f.readlines() # 전부 다 읽기
print('<파일에서 읽은 내역>', read) # 리스트로 출력됨
for line in read: # 파일 내용 그대로 출력
    print(line.replace('\n', '')) # 파일을 입력할때 \n을 입력해서 두줄 띄어지기 때문에 replace로 \n을 지워줌
    f2.write(line)

f.close()
f2.close()