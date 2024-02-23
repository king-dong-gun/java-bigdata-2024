# file: p17_fileIo.py
# desc: 파일 입출력 학습

# 컴퓨터에서 열면 무조건 닫아야 하는 것
# 1. 파일 open(), close(), / 파이썬은 안닫아도 크게 지장이 없음
# 2. 네트워크 open(), close(), / 파이썬은 안닫아도 크게 지장이 없음
# 3. DB open(or connect), close()

# 언어체계 추가 ASCII(한글 cp949), 유니코드(utf-8)
# ***************상대경로, 절대경로 *****************
f = open('./day03/sample.txt', mode= 'a', encoding='utf-8') # a(기존파일 내용 추가), w(파일 새로 생성), r(읽기) 모드 종류
# 로그등을 남길때에는 a로 작업
# 파일쓰기 진행
f.write('안녕하세요. 파이썬.\n ') # \n 한줄 띄어쓰기
f.write('모두 화이팅!!\n')

f.close() # 파이썬에서는 크게 지장없음, 다른 언어는 무조건 close() 필수