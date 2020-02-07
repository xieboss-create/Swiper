import random

import requests
from django.core.cache import cache

from swiper import conf


def get_rand_code(length=5):
    code = '0123456789'
    vscode = ''.join(random.sample(code, length))
    return vscode
def send_sms(mobile):
    '''发送短信验证码'''
    key='Vcode-%s'%mobile
    #检查短信发送状态，防止短时间内给用户重复发送短信
    if cache.get(key):
        return True
    vcode=get_rand_code()
    print('验证码: %s' % vcode)
    args=conf.YZX_SMS_ARGS.copy() # 原型模式
    args['param']=vcode
    args['mobile']=mobile

    response = requests.post(conf.YZX_SMS_API, json=args)
    if response.status_code ==200:
        result=response.json()
        print('短信发送状态: %s' % result.get('msg'))
        if result.get('code') =='000000':
            cache.set(key,vcode,600)# 给用户多预留一些时间
            return True
        else:
            return False
    return False