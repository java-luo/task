import hashlib
import time

import xmltodict
from flask import Blueprint
from flask import request, make_response

from com.itcast.service import Wx_service

wx = Blueprint("wx", __name__)


@wx.route('/wx', methods=['GET', 'POST'])
def wxx():
    if request.method == "GET":
        # 设置token
        token = 'aaa'
        # 获取参数
        data = request.args
        signature = data.get('signature')
        timestamp = data.get('timestamp')
        nonce = data.get('nonce')
        echostr = data.get('echostr')

        # 对参数进行字典排序，拼接字符串
        temp = [timestamp, nonce, token]
        temp.sort()
        temp = ''.join(temp)
        # 加密

        if hashlib.sha1(temp.encode("utf-8")).hexdigest() == signature:
            return make_response(echostr)
        else:
            return 'error', 403
    else:
        xml = request.data
        req = xmltodict.parse(xml)['xml']

        if 'text' == req.get('MsgType'):
            resp = {
                'ToUserName': req.get('FromUserName'),
                'FromUserName': req.get('ToUserName'),
                'CreateTime': int(time.time()),
                'MsgType': 'text',
                'Content': req.get('Content')
            }

        else:
            return "success"


@wx.route('/getAccessToken', methods=['GET', 'POST'])
def get_access_token():
    return Wx_service.get_access_token()

