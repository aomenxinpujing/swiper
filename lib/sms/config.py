#  setting
TIME_CACHE = 60*5
TIME_TIMEOUT = 10
#  format
FORMAT_CODE = 'User-%s'

#  sms发送结果说明
ERROR_TIMROUT = 0b0000  # 超时错误
ERROR_HTTP = 0b0001   # 请求错误
ERROR_OTHER = 0b0111  # 其他未知错误

SUCCESS_SEND = 0b1111

#  sms发送结果信息
MSG_TIMEOUT = 'timeout '
MSG_HTTP =  'http error'
MSG_OTNRT = 'other error'

MSG_SUCCESS =  'success'
