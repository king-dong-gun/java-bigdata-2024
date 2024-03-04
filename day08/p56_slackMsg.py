# file: p56_slackMsg.py
# desc: 슬랙으로 스마트폰 메시지 보내기
'''순서
1. http://api.slack.com/ 에서 Yuor apps > Create your first app
2. From Scratch 클릭 > 영어만 가능
3. 워크스페이스 선택
4. Incomming Webhooks > On > Add New webhook to Workspace 클릭 > 채널선택 > 허용
'''

import requests
import json

slack_url = 'https://hooks.slack.com/services/T06M9D*****/B06N2L*****/6H1RVVPJxv8538jmG*****' # 깃헙 업로드전 삭제 필요

headers = { 'Content-type' : 'application/json'}
data = { 'text' : 'Python에서 보낸 메세지입니다^^'}

res = requests.post(slack_url, headers=headers, data=json.dumps(data))
if res.status_code == 200 :
    print('메시지 전송성공^^')
else :
    print('메시지 전송실패ㅠㅠ')