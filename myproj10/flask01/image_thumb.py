# pip install pillow
# 이미지 압축
from PIL import Image

# PIL : Python Image Library

im = Image.open("static/hamjji.jpg")
im.thumbnail((800, 600))
im.save("static/hamjji.jpg")
