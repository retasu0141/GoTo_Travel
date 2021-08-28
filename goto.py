import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFilter,ImageFont

#背景画像(RGB指定)
height = 452
width = 452
blank = np.zeros((height, width, 3))
blank += [200,200,255][::-1] #RGBで青指定

cv2.imwrite('blank.png',blank)

#旗みたいな奴の色(白推奨)
#452*452の画像一枚あれば良いので最初の一回だけ実行 その後コメントあうと
"""
height = 452
width = 452
blank = np.zeros((height, width, 3))
blank += 255 #←全ゼロデータに255を足してホワイトにする

cv2.imwrite('White.png',blank)
"""


im1 = Image.open('blank.png')
#背景画像読み込み
im2 = Image.open('White.png')
#旗のやつの色読み込み
mask_im = Image.open('goto.png').resize(im1.size)
#GoToトラベルの透過素材読み込み


back_im = im1.copy()
back_im.paste(im2, mask_im)

#back_im.save('goto2.jpg', quality=95)
#透過文字入れする前の素材


#文字入れの関数 https://qiita.com/xKxAxKx/items/2599006005098dc2e299 のほぼコピペ
def add_text_to_image(img, text, font_path, font_size, font_color, height, width, max_length=740):
    position = (width, height)
    font = ImageFont.truetype(font_path, font_size)
    draw = ImageDraw.Draw(img)
    if draw.textsize(text, font=font)[0] > max_length:
        while draw.textsize(text + '…', font=font)[0] > max_length:
            text = text[:-1]
        text = text + '…'

    draw.text(position, text, font_color, font=font,anchor='mm')

    return img



song_title = "入れたい文字"
font_path = "フォント指定"
#ここから下はいじらないほうが良いかも
font_size = 80
font_color = (255, 255, 255)
height = 350
width = 220
img = add_text_to_image(back_im, song_title, font_path, font_size, font_color, height, width)

img.save('goto2.jpg')
