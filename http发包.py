import json

from pip._vendor.requests.sessions import Session

global username, password, token
username = 'xxxxx'
password = 'xxxxx'
s = Session()


# python2.x与python3.x差别非常大
# 过去使用urllib，urllib2，现在使用request包

def showCookie(cookies):
    for i in cookies:
        print(i)
        i.domain = '*'
    print('*' * 20)


# 第一步，访问百度，获取cookie百度UID
s.get("http://www.baidu.com")
# 第二步，访问密码网页，获取token，此页面返回一个json串。后面的参数不同返回的结果不同，抓包之后，尝试着删除了许多没用的参数
resp = s.get("https://passport.baidu.com/v2/api/?getapi&tpl=mn&apiver=v3")
# 必须把单引号转化成双引号，否则无法通过json进行解析，python3.x开始走向严格和规范了
t = json.loads(resp.text.replace('\'', '\"'))
token = t['data']['token']
# 第三步，提交表单。经过测试，只有下面五个数据是必需的
data = {
    "token": token,
    "tpl": "mn",
    "loginmerge": True,
    "username": username,
    "password": password
}
resp = s.post("https://passport.baidu.com/v2/api/?login", data) 
resp = s.get("http://tieba.baidu.com/dc/common/tbs")
tbs = json.loads(resp.text)['tbs']
data = {
    "kw": "大学生励志", #贴吧
    "fid": "1847502",  # first post id
    "tid": "4135933166",  # 帖子id
    "tbs": tbs,  # 很重要
    "content": "现在下午两点四十二" # 帖子内容
}
resp = s.post("http://tieba.baidu.com/f/commit/post/add",data)
print(resp.text)
print("over")
