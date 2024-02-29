# file: p42_jsonHandle.py
# desc: json 읽고 쓰기

import json

## json 읽기
# file 읽어서 쓸 객체변수 f, file, fp
# with문으로 작업하면 fp.close() 불필요
with open('./day07/p40_testData.json', mode='r', encoding='utf-8') as fp :
    data = json.load(fp)


# data로 출력 -> 파이썬의 dictionary로 출력
# json.dumps(data)로 출력 -> json으로 출력
# indent='\t' -> 더 보기좋게 출력
print(json.dumps(data, indent='\t'))
jData = json.dumps(data) # json 스타일의 문자열

# json 데이터 접근은 파이썬 dictionary, list와 동일하게 사용가능
print(data['name'])
print(data['freind'][0]) # data의 frined의 0번째 배열 출력

## json 쓰기
# dictionary 생성 -> json dump후 저장
soccer = dict()

ManU = dict()
ManU['LigueWinner'] = 20
ManU['UclWineer'] = 3
ManU['TopPlayer'] = 'Bruno'
soccer['ManU'] = ManU

Tottenham = dict()
Tottenham['LigueWinner'] = 0
Tottenham['UclWineer'] = 0
Tottenham['BestPlayer'] = 'Maddison'
soccer['Tottenham'] = Tottenham

# json 파일 저장
with open('./day07/soccer.json', mode='w', encoding='utf-8') as fp :
    json.dump(soccer, fp, indent='\t', ensure_ascii=True)




