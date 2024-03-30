# encoding='utf-8

# @Time: 2024-01-06
# @File: %
#!/usr/bin/env
from icecream import ic
import os

class WriteLogo:
    def __init__(self, path):
        self.path = path

    def writeLogo(self, logo):
        with open(self.path, 'a', encoding='utf-8') as f:
            f.write(logo)
            f.write('\n')

    def readLogo(self):
        with open(self.path, 'r', encoding='utf-8') as f:
            logo = f.read()
            return logo

    def deleteLogo(self):
        os.remove(self.path)
if __name__ == '__main__':
    log = WriteLogo('./logo.txt')
    txt = "hello world" + '\t' + str(1)
    texts = log.readLogo().split('\n')
    ic(texts)
    for text in texts:
        if text != '':
            search_text, page = text.split('\t')
            ic(search_text, page)


    
    # log.writeLogo(txt)
    # log.writeLogo(txt)
    # log.writeLogo(txt)




