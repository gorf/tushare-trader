#!/usr/bin/env python
# -*- coding:utf-8 -*- 

'''
Created on 2016年10月1日
@author: Jimmy Liu
@group : waditu
@contact: jimmysoa@sina.cn
'''

import json
import time
import six
from tushare.trader import vars as vs
import os
DIR = os.path.dirname(os.path.abspath(__file__))
DEBUG = os.path.isfile(os.path.join(DIR,'.debug'))
def nowtime_str():
    return time.time() * 1000


def get_jdata(txtdata):
    txtdata = txtdata.content
    if six.PY3:
        txtdata = txtdata.decode('utf-8')
    jsonobj = json.loads(txtdata)
    return jsonobj
        
        
def get_vcode(broker, res):
    from PIL import Image
    import pytesseract as pt
    import io
    if broker == 'csc':
        imgdata = res.content
        img = Image.open(io.BytesIO(imgdata))
        img = img.crop(box=(0,0,50,20))
        if DEBUG:
            img.show()
        vcode = pt.image_to_string(img, config='-psm 7 zxjt')
        print(vcode)
        try:
            vcode = eval(vcode)
        except SyntaxError:
            code_strings = vcode.split()
            #print(code_strings)
            codes = [int(i) for i in code_strings]
            vcode = sum(codes)
        print(vcode)
        return vcode
    
