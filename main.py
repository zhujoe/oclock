import time
import os
from aip import AipSpeech


# 初始化
def init_baidu():
    APP_ID = '9975737'
    API_KEY = 'U490hthRy5e6MfQWHWHV8GXB'
    SECRET_KEY = 'f77652d7834398c678a6b39016de2048'
    aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    return aipSpeech

# 获取当前时间
def get_now_time():
    return time.strftime('%H:%M:%S', time.localtime(time.time()))


# 百度文字转语音方法
def baidu_speak(aipSpeech, strwords):
    wel = aipSpeech.synthesis(strwords, 'zh', 1, {'vol': 3, 'per': 4})
    if not isinstance(wel, dict):
        with open('time.mp3', 'wb') as f:
            f.write(wel)
    os.system('time.mp3')

if __name__ == '__main__':
    airspeed = init_baidu()
    while True:
        nowtime = get_now_time()
        # print(nowtime)
        times = nowtime.split(':')
        if times[1] == '00' and times[2] == '00':
            times[0] = times[0].replace('0', '')
            strs = '现在时间，' + times[0] + '点整'
            baidu_speak(airspeed, strs)
        time.sleep(1)
