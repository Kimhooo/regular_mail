import smtplib
import requests, json
import datetime
#coding=gbk
from email.mime.text import MIMEText
mail_host = 'smtp.qq.com'  
mail_user = '32*****9'#填写你的QQ号  
mail_pass = 'usq*****ghg'  #填写你的QQ邮箱授权码   
sender = '32*****9@qq.com' #填写你的QQ邮箱  
receivers = ['32*****9@qq.com'] #填写收件方的邮箱  

stremoji1="(੭•̀ω•́)੭"
stremoji2="( ͡° ͜ʖ ͡°)✧"
stremoji3="[○･｀Д´･ ○]"
stremoji4="٩(๑>◡<๑)۶"
stremoji5="ヾ(≧▽≦*)o"
stremoji6=" (｡･∀･)ﾉﾞ"
stremoji7="w(ﾟДﾟ)w"

#土味情话接口
url = 'http://api.tianapi.com/txapi/saylove/index' # 接口地址
d ={'key':'53919*****2787'} # 填入你申请的key
rep = requests.get(url,d) # 发送请求
str10="\n\n今日份土味，请查收：\n"
str11=rep.json()["newslist"][0]["content"]

#天气状况接口
url1 = 'https://devapi.qweather.com/v7/weather/3d?'# 接口地址
d1 ={'location':'101280109','key':'329a97*****c24'}# 填入地址id，你申请的key
rep1 = requests.get(url1,d1)
strMax=rep1.json()["daily"][0]["tempMax"]
strMin=rep1.json()["daily"][0]["tempMin"]
strtextDay=rep1.json()["daily"][0]["textDay"]
strwindScaleDay=rep1.json()["daily"][0]["windScaleDay"]
strsunset=rep1.json()["daily"][0]["sunset"]
strmoonPhase=rep1.json()["daily"][0]["moonPhase"]


#星座运势接口
url2 = 'http://web.juhe.cn:8080/constellation/getAll?'# 接口地址
d2 ={'key':'3aa929e22*****03182','type':'today','consName':'天蝎座'}# 填入你申请的key，类型选择今天，填入要查找的星座
rep2 = requests.get(url2,d2)
strAll=rep2.json()["all"]
strhealth=rep2.json()["health"]
strlove=rep2.json()["love"]
strmoney=rep2.json()["money"]
strwork=rep2.json()["work"]
strlove=rep2.json()["love"]
strsummary=rep2.json()["summary"]


#笑话大全接口
url3 = 'http://v.juhe.cn/joke/randJoke.php'
d3 ={'key':'c5953ba5a*****137ff8da29ff8'}
rep3 = requests.get(url3,d3)
strJoke=rep3.json()["result"][0]["content"]


#历史上的今天接口
strMonth=datetime.datetime.now().month #获取月份
strDay=datetime.datetime.now().day  #获取日期
url4 = 'http://api.juheapi.com/japi/toh'
d4 ={'v':'2.0','month':strMonth,'day':strDay,'key':'3294092bb2*****c63988db9'}
rep4 = requests.get(url4,d4)
strHistory=rep4.json()["result"][0]["des"]


str1="今天是"
str2=datetime.datetime.now().strftime('%Y-%m-%d,%A')
str3="\n\n接下来是天气预报环节啦ᶘ ᵒᴥᵒᶅ\n广州今天是:"+strtextDay+",最高温度："+strMax+",最低温度："+strMin+",风力等级："+strwindScaleDay
str4="\n傍晚太阳将会在"+strsunset+"缓缓落下，记得早点回家！今晚你能看到的月亮是："+strmoonPhase

str5="\n\n天蝎座今日运程"+stremoji5+"：\n综合指数："+strAll+"\n爱情指数："+strlove+"\n健康指数："+strhealth+"\n财运指数："+strmoney+"\n工作指数："+strwork+"\n迷信环节"+stremoji2+"：\n"+strsummary


str6="\n\n今日笑话时间：\n"+strJoke

str7="\n你可能不知道，"+strHistory+stremoji7

str8="\n\n爱你"+stremoji4+"傻子！！！"

str9="\n\n发自我的 iPhone12 Promax 512G海军蓝镶钻防弹全球限量版"

str999=str1+str2+stremoji1+str7+str3+str4+str5+str6+str10+str11+str8+str9

message = MIMEText(str999,'plain','utf-8')
message['Subject'] = str2
message['From'] = sender 
message['To'] = receivers[0]  

try:
    smtpObj = smtplib.SMTP() 
    smtpObj.connect(mail_host,25)
    smtpObj.login(mail_user,mail_pass) 
    smtpObj.sendmail(
        sender,receivers,message.as_string()) 
    print('send success')
except smtplib.SMTPException as e:
    print('send error',e) 
