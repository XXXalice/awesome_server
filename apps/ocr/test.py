from ocr_api import Ocr

ocr = Ocr()
ocr.read_img(input())
ocr.img_effect('gray', show=True)
str = ocr.img_to_str(lang='jpn', tesseract_layout=6)
print(str)