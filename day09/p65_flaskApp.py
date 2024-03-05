# file: p65_flaskApp.py
# desc: 플라스크 웹 서버

'''
pip3 install flask
'''

from flask import Flask, render_template

app = Flask(__name__) # 현재 모듈로 Flask 앱 생성

@app.route('/') # 루트 URL에 대한 뷰 함수
def hello() :
    return('Hello, Flask!!')

@app.route('/unit')
def testPage1() :
    return render_template('unit.html')

@app.route('/naver')
def testPage2() :
    return render_template('register.html')

def main() :
    app.run(debug=True, port=8080)

if __name__ == '__main__' :
    main()

