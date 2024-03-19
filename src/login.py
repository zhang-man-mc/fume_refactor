from src.request_.request import request_post,request_get
import time
import json
import base64

from .account import Account 

def get_time():
    # 毫秒妙级时间戳 13位数字
    now_time = str(int(time.time()*1000))
    return now_time

def get_photo_url(url):
    return url + get_time()



def base64_api(img):
    # 返回账号密码
    a = Account()
    uname,pwd = a.account,a.password
    with open(img, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        b64 = base64_data.decode()
    data = {"username": uname, "password": pwd, "typeid": 2, "image": b64}
    result = json.loads(request_post("http://api.ttshitu.com/predict", data))
    if result['success']:
        return result["data"]["result"]
    else:
        #！！！！！！！注意：返回 人工不足等 错误情况 请加逻辑处理防止脚本卡死 继续重新 识别
        return result["message"]
    return ""



def login_fume_web():
    # 请求验证码地址
    # 构造时间戳
    # 拼接url
    # 识别验证码
    url_photo = get_photo_url('http://xhhb.senzly.cn/servlet/Vcode_new.serv?t=')
    response = request_get(url_photo)         # 图片为二进制数据
    image_data = response.content
    with open('Vcode.jpg',mode='wb') as f:
        f.write(image_data)
    # 验证码结果
    v_code_result = base64_api('Vcode.jpg')


    play_load = {
        "account": "9SUBjEeNy7nFMzk123",
        "password": "6SUBIyusanb170e13a221a4cb58c66876006488504",
        "vcode": v_code_result
    }

    url_jump = 'http://xhhb.senzly.cn/cusLogin.php'
    request_post(url_jump,play_load)
    print('登录成功')

    # return session
    # 个人验证


if __name__ == '__main__':
    login_fume_web()