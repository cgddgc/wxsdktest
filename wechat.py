#coding=utf-8
import werobot,urllib,requests,json

#token="cgddgc"
#robot.config['HOST']='0.0.0.0'
#robot.config['PORT']=8998

robot=werobot.WeRoBot()
robot.config.from_pyfile(".weconfig")

def TulingRobot(message):
    url = "http://www.tuling123.com/openapi/api"#'http://www.xiaodoubi.com/bot/chat.php'
    r = requests.post(url, data={'key':"b8bb8bf591af8b522652fc2aa1e4a03a",'info':message.content,'userid':message.source})
    result=(json.loads((r.text))["text"])
    return result

@robot.text
def responText(message):
    return TulingRobot(message)

@robot.image
def resp2(message):
    return message.img

@robot.location
def resp3(message):
    return message.label


robot.run(server='twisted')