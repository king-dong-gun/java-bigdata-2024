# file: p46_tts.py
# desc: Text To Speech

# pip3 install gTTs
# pip3 install playsound2
from gtts import gTTS

text = input('소리로 바꿀 텍스트 입력 > ')

speech = gTTS(text=text, lang='ko')
speech.save('./day07/tts.mp3')
