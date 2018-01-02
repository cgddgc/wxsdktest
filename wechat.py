#coding=utf-8
import werobot,urllib,requests,json,re,random,urllib.parse,urllib.request,sys,base64,os,types,time,pymysql
import util
from wxcfg import MyConfig
from Crypto.Cipher import AES
from cloud_music import cloud_music

robot=werobot.WeRoBot(token="cgddgc")

#robot.config.from_pyfile("wxcfg.py")
#robot.config.from_object(MyConfig)
robot.config['HOST']='0.0.0.0'
robot.config['PORT']=8998


@robot.text
def responText(message):
    util.record(message.source,message.content,time.strftime('%Y-%m-%d %H:%M:%S'))
    key=message.content
    music=cloud_music()
    if '~' in key or '来首' in key:
        kw=key.replace("~","").replace('来首','')
        return util.reply_music(kw)
    else:
        return util.TulingRobot(key,message.source)

@robot.voice
def respon_voice(message):
    key=message.recognition
    util.record(message.source,message.recognition,time.strftime('%Y-%m-%d %H:%M:%S'))
    if not key==None:
        if '来首' in key or '点歌' in key:
            kw=key.replace('来首','').replace('点歌','')
            return util.reply_music(kw)
        else:
            return util.TulingRobot(key,message.source)
    else:
        return '听不清，大点声'

@robot.subscribe
def subscribe(message):
    return '谢谢关注，发送~或来首+歌名点歌，歌名后可加*指定歌手，发送文字或语音可以和我尬聊'

@robot.image
def resp2(message):
    return message.img

@robot.location
def resp3(message):
    return message.label


robot.run()
