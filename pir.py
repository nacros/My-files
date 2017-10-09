import os
import time
from TwitterAPI import TwitterAPI
from gpiozero import MotionSensor

pir = MotionSensor(4)
b=1
CONSUMER_KEY = 'Ne0uvWoo6CxdpboDrj23XCAYC'
CONSUMER_SECRET = 'UCpmH9IoXQoCB0Iof1HJ3YGSdjAMkvEkLMY7yKsKLnpr4v8ZNl'
ACCESS_TOKEN_KEY = '912253833329258497-RVmLvPdBUg1Ssfv7ijXeukfjNsEnH6F'
ACCESS_TOKEN_SECRET = 'nDSSXVmNvKJtqVXZmHtnjoTRxeWaEhWoxnSvOUxHmrvz8'
api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)

while True:
    if pir.motion_detected:
        img="/home/pi/cam/imgs.jpg"
        cmd= "fswebcam -F 3 --fps 20 -r \"1200x800\" "+img
        os.system(cmd)
        print("pic taken")
        file = open(img, 'rb')
        data = file.read()
        r = api.request('statuses/update_with_media', {'status':'#pyTweetCMR'}, {'media[]':data})
        print(r.status_code)
