import ssl
from qcloudsms_py import SmsSingleSender
from qcloudsms_py.httpclient import HTTPError
import random




appid ='1400746461'  # 准备工作中的SDK AppID，类型：int
appkey = 'ca16e8f017bafbf005aba138b0eb8340'   # 准备工作中的App Key，类型：str
phone_num = 15829303933
sign1 = '我的爱好分享个人网'  # 准备工作中的应用签名，类型：str
#验证码生成
code = ''
for item in range(6):
    code += str(random.randint(0, 9))
#print(code)

#发送
ssender = SmsSingleSender(appid,appkey)
# {86, phone_num, template_id, template_param_list, sign=sms_sign}
rzb = ssender.send_with_param(86, phone_num, 1567599, ['3803'], sign = sign1, extend ='', ext ='')
print(rzb)      