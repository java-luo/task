import requests

from com.itcast.utils import RedisUtil, iniUtil, my_message


# 微信公众号业务类

# 获取微信access_token
def get_access_token():
    appid = iniUtil.getInI("wx", "appid")
    secret = iniUtil.getInI("wx", "secret")
    access_token = RedisUtil.get("access_token")
    if access_token is None:
        url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s" % (
            appid, secret)
        r = requests.get(url)
        try:
            # 获取accessToken
            access_token = r.json()['access_token']
            # 把最新的access_token放到缓存当中 设置火气时间
            RedisUtil.set("access_token", access_token, 7000)
        except  Exception as e:
            my_message.ifttt_send_meaasge({"value1", "获取access_token异常" + r.json()["errcode"]})
    else:
        access_token = access_token.decode()
    return access_token


# 获取微信公众号的粉丝
def get_wx_user_list():
    url = "https://api.weixin.qq.com/cgi-bin/user/get?access_token=" + get_access_token()
    r = requests.get(url)
    # 获取用户Id列表
    user_openid_list = r.json()['data']['openid']
    return user_openid_list


# 发送模板消息
def send_template_msg(data):
    url = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=%s" % get_access_token()
    r = requests.post(url, json=data)
    if 0 != r.json()["errcode"]:
        msg = "发送模板消息失败,微信返回的状态码为:%s" % r.json()["errcode"]
        raise Exception(msg)
        return "error"
    else:
        return "success"
