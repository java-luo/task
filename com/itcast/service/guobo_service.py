import requests
from com.itcast.utils import SpiderUtil
from com.itcast.utils import iniUtil

"""查询国博余票"""
def get_ticket_list():
    url=iniUtil.getInI("spider","get_ticket_num_url")
    headers = {
        "Referer": "http://ticket.chnmuseum.cn/yuyue/index",
        "Origin": "http://ticket.chnmuseum.cn",
        "User-Agent": SpiderUtil.get_user_agent()
    }
    r = requests.get(url, headers=headers)
    return r.json()