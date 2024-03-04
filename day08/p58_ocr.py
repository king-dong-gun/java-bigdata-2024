# file: p58_ocr.py
# desc: 이미지 내 글자 인식

'''
> pip3 install pytesseract
'''
from PIL import Image
import pytesseract as pt

imgPath = './images/ManUNews.png'
im = Image.open(imgPath)
im.show()

pt.pytesseract.tesseract_cmd = '/opt/homebrew/Cellar/tesseract/5.3.4_1/bin/tesseract'
text = pt.image_to_string(Image.open(imgPath), lang='kor')

print(text)