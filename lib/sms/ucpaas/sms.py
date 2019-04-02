import random
import requests
from django.core.cache import cache
from requests import Timeout, HTTPError

from lib.sms import config as sms_config
from lib.sms.ucpaas import config, variable
from commen.keys import CODE_KEY


def gen_code(length=4):
    start = 10 ** (length - 1)
    end = 10 ** length - 1
    code = str(random.randint(start,end))
    return code


def send_sms(phone_num):
    code = gen_code()
    url = config.YZX_SMS_API
    params = config.YZX_SMS_PARAMS

    params['mobile'] = phone_num
    params['param'] = code

    result = (None, None)

    try:
        response = requests.post(url, json=params, timeout=sms_config.TIME_TIMEOUT)
        response.raise_for_status()
    except Timeout:
        result = (sms_config.ERROR_TIMROUT, sms_config.MSG_TIMEOUT)
    except HTTPError:
        result = (sms_config.ERROR_HTTP, sms_config.MSG_HTTP)
    except Exception as e:
        result = (sms_config.ERROR_OTHER, sms_config.MSG_OTNRT)
    else:
        response_json = response.json()

        if response_json['code'] == variable.SUCCESS_CODE:
            result = (sms_config.SUCCESS_SEND, code)
            cache.set(CODE_KEY % phone_num, code, sms_config.TIME_CACHE)
        else:
            result = (sms_config.ERROR_OTHER,response_json.get('msg', 'CODE ERROR'))
    return result



