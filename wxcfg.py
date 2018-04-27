#!coding=utf-8
import pymysql
from werobot.session.mysqlstorage import MySQLStorage

class GlobalConfig():
    dbconf={'host':'127.0.0.1','port':3306,'user':'gxd','password':'cgd626723','db':'wechat','charset':'utf8','cursorclass':pymysql.cursors.DictCursor}
    sess_cnn1=pymysql.connect(user='gxd',password='cgd626723',db='werobot1',host='127.0.0.1',charset='utf8')
    sess_cnn2=pymysql.connect(user='gxd',password='cgd626723',db='werobot2',host='127.0.0.1',charset='utf8')
    TulingKey="b8bb8bf591af8b522652fc2aa1e4a03a"
    Myproxy={"http":"47.106.94.152:6667"}
    agents=[
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
            "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
            "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
            "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
            "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
            "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
            "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
            "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
            "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0"
        ]
    owner=['oVdu6swIuCYPoiKN6NGXz2UAxmmo','odd2gjtRc-ohwDhgqi19sn5Z5kUE']

class RobotConfig():
    TOKEN="cgddgc"
    SERVER="waitress"
    HOST="0.0.0.0"
    PORT=8998
    SESSION_STORAGE=False
    #MySQLStorage(GlobalConfig.sess_cnn1)
    APP_ID='wx03b529f87a6d25a7'
    APP_SECRET='678d29e1b19f6e5a3beb110e9699b136'
    ENCODING_AES_KEY=None#'K5ayqJ75ryU6vtOfo5VkVPOU9jt4iCCURu5X2X043mM'

class cgddgcConfig():
    TOKEN="cgddgc"
    SERVER="waitress"
    HOST="0.0.0.0"
    PORT=8898
    SESSION_STORAGE=False
    #MySQLStorage(GlobalConfig.sess_cnn2)
    APP_ID="wxa6e5e8cff31cd69c"
    APP_SECRET="84c79f1157f3c5ee9e329faa7d6eac4a"
    ENCODING_AES_KEY='K5ayqJ75ryU6vtOfo5VkVPOU9jt4iCCURu5X2X043mM'

class DefaultResponseMsg():
    noPermission='permission denied'+'\n'+'您无权执行此操作'
    musicMode='点歌模式'
    chatMode='对话模式'
    commanMode='命令行模式'
    subscribe='谢谢关注，分别输入点歌模式，对话模式，命令行模式进入相应模式（默认对话模式），输入openid获取当前账号id'
    unexpectedError='未知错误'
    musicNotFound='什么都没找到，换一首吧'
    nullKey='关键字不能为空'
    song='采茶纪'
    noMusicUrl='啊哦，什么都没找到，可能服务器开小差了，要不换一首吧'