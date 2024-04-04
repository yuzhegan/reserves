# encoding='utf-8

# @Time: 2024-04-04
# @File: %
#!/usr/bin/env
from icecream import ic
import os
import requests


img_list = ['https://cdn1.ozone.ru/s3/multimedia-n/6895330187.jpg', 'https://cdn1.ozone.ru/s3/multimedia-1-f/6922800051.jpg']

def download_img(url):
    img = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    with open(f'{os.path.basename(url)}', 'wb') as f:
        f.write(img.content)
        print(f'Image {os.path.basename(url)} downloaded')
    print('Download complete')

for img in img_list:
    download_img(img)
