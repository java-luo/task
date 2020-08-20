import requests
from com.itcast.utils import SpiderUtil
from com.itcast.utils import iniUtil
from com.itcast.splider import keji_spider
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

def get_shoudu_ticket_list():
    headers = {
        "Referer": "https://sdbwg.hdwbcloud.com/",
        "Host": "sdbwg.hdwbcloud.com",
        "User-Agent": SpiderUtil.get_user_agent(),
        "X-XSRF-TOKEN":"eyJpdiI6ImxIYWRWZFhhSHFWQXNDYytCWkhWamc9PSIsInZhbHVlIjoiZlpydEVRQVNYN1B5ZGs4bnVoRlRTSWwzV0Zya1phdW8xWVZLRXRrcm9yMnllSzFreVRjRnFNWllCTlI0Q3MrYyIsIm1hYyI6IjVkN2RhMGZiM2Y0MTNkMDRkMDVjMTI0ZTQzY2M1OTY5OTE4Nzk3MjhkNmFkZGNkNDQyMWI1MGZhM2Y5M2UyM2UifQ=="
    }
    r = requests.get("https://sdbwg.hdwbcloud.com/api/ticket/calendar?p=w", headers=headers)
    return r.json()

def get_Keji_ticket():
    return keji_spider.get_ticket_list()


