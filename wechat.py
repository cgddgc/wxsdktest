#coding=utf-8
import werobot

token="cgddgc"

robot=werobot.WeRoBot(token=token)
'''
def TulingRobot(message):
    url = "http://www.tuling123.com/openapi/api"#'http://www.xiaodoubi.com/bot/chat.php'
    r = requests.post(url, data={'key':"b8bb8bf591af8b522652fc2aa1e4a03a",'info':"lalala",'userid':"cgddgc"})
    result=(json.loads((r.text))["text"])
    return result
'''

@robot.text
def hl(message):
    print(message)
    return message.content+"蠢材"

@robot.image
def h2(message):
    return message.img

robot.config['HOST']='0.0.0.0'
robot.config['PORT']=8998
robot.run()