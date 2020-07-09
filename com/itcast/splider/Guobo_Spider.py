import requests

from com.itcast.utils import RedisUtil,SpiderUtil,iniUtil,my_message

headers = {
    "Referer": "http://ticket.chnmuseum.cn/yuyue/index",
    "Origin": "http://ticket.chnmuseum.cn",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "User-Agent": SpiderUtil.get_user_agent()
}

# 到多少以下开始提醒
WARN_NUMBER = 50

# redis过期时间 十天
ex_time = 60 * 60 * 24 * 10


# 获取国家博物馆票数据
def get_ticket():
    url = iniUtil.getInI('spider', 'get_ticket_num_url')
    #
    try:
        reponse = requests.get(url, headers=headers)
        if reponse.status_code != 200:
            message = "国博请求异常,HTTP响应码:%s" % reponse.status_code
            # 发送提醒
            my_message.ifttt_send_meaasge({"value1": message})
        if reponse.json()['status'] != 1:
            message = "国博请求异常,JSON响应码为:%s" % reponse.json()['status']
            # 发送提醒
            my_message.ifttt_send_meaasge({"value1": message})
    except Exception as e:
        # 发送提醒
        message = "国博程序发生异常:%s" % e
        my_message.ifttt_send_meaasge({"value1": message})
    return reponse.json()


# 解析国家博物馆票数据
def analysis(data):
    # 返回结果集  内包含场次dict  票量dict
    result_dict = {}
    # 场次信息
    ticket_date = {}

    ticket_tps = data['data']['tps']
    for tps in ticket_tps:
        # 获取各个场次
        ticket_date[tps['tp_id']] = tps['time_period_show']
        result_dict['ticket_date'] = ticket_date

    result_dict['ticket_number'] = data['data']['yy_date']
    return result_dict


# 检查票量
def check_ticket_number(ticket_number, ticket_date):
    for ticket in ticket_number:
        # print("日期%s 票量%s" % (ticket['t_date'], ticket['tp_last_stock_sum']))
        for t in ticket['tp']:
            if t['tp_last_stock'] < WARN_NUMBER:
                try:
                    if RedisUtil.get(t['td_tp_id']) is None:
                        value = ticket['t_date'] + " " + ticket_date[t['tp_id']]
                        RedisUtil.set(t['td_tp_id'], value, ex_time)
                        msg = "%s日%s场,仅剩余%s张,注意关班!!!" % (ticket['t_date'], ticket_date[t['tp_id']], t['tp_last_stock'])
                        print(msg)
                        # todo: 上线时放开提醒
                        my_message.ifttt_send_meaasge({"value1": msg})
                        # my_message.wechat_send_meaasge({"text", msg})
                except Exception as e:
                    my_message.ifttt_send_meaasge({"value1": e})
                    return False

    return True


def start():
    data = get_ticket()
    analysis_data = analysis(data)
    isOk = check_ticket_number(analysis_data['ticket_number'], analysis_data['ticket_date'])
    return isOk
