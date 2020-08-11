import re
import requests
import time
from bs4 import BeautifulSoup

from com.itcast.utils import SpiderUtil
from com.itcast.utils import my_message
from com.itcast.utils import validCodeUtil

headers = {
    "User-Agent": SpiderUtil.get_user_agent(),
    "Content-Type": "application/x-www-form-urlencoded",

}
login_headers = {
    "User-Agent": SpiderUtil.get_user_agent(),
    "Content-Type": "application/json;charset=UTF-8"
}

r = requests.session()


def login():
    global r
    response = r.get("http://ticket.cdstm.cn/vcode/1", headers=headers)
    validCode = validCodeUtil.TestFunc(response.content)
    loginData = {
        "userName": "13261063222",
        "password": "l199512",
        "validCode": validCode
    }
    loginResponse = r.post("http://ticket.cdstm.cn/login/in", json=loginData, headers=login_headers)

    #print("登录:", loginResponse.json())


def getIndex():
    # 获取科技馆日期
    indexReponse = r.get("http://ticket.cdstm.cn/index", headers=headers)
    b = BeautifulSoup(indexReponse.content, "html.parser")
    div = b.find("div", {"class": "calend"})
    list_i = div.find_all("i", attrs={"data-year": re.compile("/*")})
    inData = []
    for i in list_i:
        if i.text.find("闭馆") == -1:
            inData.append(i["indate"])
    return inData


def getTicket(Indate):
    beforeData = {
        "inDate": Indate,
        "isToDay": "false"
    }
    response = r.post("http://ticket.cdstm.cn/buy/before", headers=headers, data=beforeData)
    soup = BeautifulSoup(response.content, "html.parser")
    if soup.find("title").text == "登录":
        login()
        getTicket(Indate)
        return
    else:
        print("查询票数页面:", soup.find("title").text)
        date = soup.find("div", {"class": "tick"}).h3.text.strip()
        date = re.findall("\d{4}-\d{2}-\d{2}", date)[0]
        try:
            # 获取票数表格
            td_list = soup.find("table").find_all("td")
            # 获取上午票数
            morning = td_list[2].text.strip()
            # 获取下午票数
            afternoon = td_list[4].text.strip()
        except:
            return
        ticket = {
            "date": date,
            "morning": morning,
            "afternoon": afternoon
        }
        return ticket


# 获取票数
def get_ticket_list():
    print("获取科技馆票数")
    dateList = getIndex()
    ticket_list = []
    for date in dateList:
        time.sleep(0.5)
        ticket = getTicket(date)
        if ticket != None:
            ticket_list.append(ticket)
        else:
            pass
    return ticket_list


def keep_link():
    try:
        res = r.get("http://ticket.cdstm.cn/user/center/baseInfo", headers=headers)
        # soup = BeautifulSoup(res.content, "html.parser")
        # title = soup.find("title").text
        # print("保持登录:", title)
    except e:
        my_message.wechat_send_meaasge({"text": e})
