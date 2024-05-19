from paddleocr import PaddleOCR,draw_ocr
import os
# Paddleocr supports Chinese, English, French, German, Korean and Japanese.
# You can set the parameter `lang` as `ch`, `en`, `fr`, `german`, `korean`, `japan`
# to switch the language model in order.
ocr = PaddleOCR(use_angle_cls=True, lang='japan') # need to run only once to download and load model into memory
img_path = 'img_test/1.rawkuma.com.jpg'
img_name = os.path.basename(img_path).split('.jpg')[0] + "_result.jpg"
#img_output = img_name + "_result.jpg"
#result = ocr.ocr(img_path, cls=True)
result = ocr.ocr(img_path)
#result = ocr.ocr(img_path, det=False)  #Only perform recognition
#result = ocr.ocr(img_path, rec=False)  #Only perform detection
# result = ocr.ocr(img_path, cls=False)  Only perform score

for line in result:
    print(line)


# draw result
from PIL import Image
result = result[0]
image = Image.open(img_path).convert('RGB')
boxes = [line[0] for line in result]
txts = [line[1][0] for line in result]
scores = [line[1][1] for line in result]
im_show = draw_ocr(image, boxes, txts, scores, font_path='./fonts/simfang.ttf')
im_show = Image.fromarray(im_show)
im_show.save(img_name)