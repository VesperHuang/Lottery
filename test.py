# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 09:44:25 2018

@author: Vepser
"""
import os
import requests
import hashlib

url='https://code.ziqiangxuetang.com/django/django-tutorial.html'
html = requests.get(url).text.encode('utf-8-sig')
md5 = hashlib.md5(html).hexdigest()

if os.path.exists('old_md5.txt'):
    with open('old_md5.txt','r') as f:
        old_md5 = f.read()
    with open('old_md5.txt','w') as f:
        f.write(md5)
else:
    with open('old_md5.txt','w') as f:
        f.write(md5)

print(md5)
print(old_md5)
        
if md5 != old_md5:
    print('資料已更新....')
else:
    print('資料未更新,從資料庫讀取')

