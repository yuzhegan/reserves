# encoding='utf-8
# @Time: 2024-01-04
# @File: %
#!/usr/bin/env
from icecream import ic
import os
import ddddocr
ocr = ddddocr.DdddOcr(old=True)
with open("./yzm.png", 'rb') as f:
    image = f.read()
res = ocr.classification(image)
print(res)
