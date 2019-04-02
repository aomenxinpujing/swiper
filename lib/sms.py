import random
import requests
from django.core.cache import cache

from swiper import config
from commen.keys import CODE_KEY
from worker import celery_app


def gen_code(length=4):
    start = 10 ** (length - 1)
    end = 10 ** length - 1
    return str(random.randint(start,end))



@celery_app.task
def send_sms(phonenum):
    code = gen_code()
    cache.set(CODE_KEY % phonenum, code, 300)
    url = config.YZX_SMS_API
    params = config.YZX_SMS_PARAMS.copy()
    params['mobile'] = phonenum
    params['param'] = code
    response = requests.post(url,json=params)
    if response.status_code == 200:
        result = response.json()
        if result['code'] == '000000':
            return True, result['msg']
        else:
            return False, result['msg']
    else:
        return '短信接口通信有误'