import threading
import time

from com.itcast.task.MonitorTicket import MonitorTicket
from com.itcast.utils import Const
from com.itcast.utils import iniUtil
from com.itcast.utils import my_message


# 初始化任务列表
def init_task_list():
    # 添加任务到任务列表当中
    guobo_task = MonitorTicket("监视国博余票")
    Const.task_list.append(guobo_task)


# 执行任务
def start_task():
    # 获取任务执行间隔时间
    sleep_time = int(iniUtil.getInI("spider", "sleep_time"))
    try:
        while True:
            for task in Const.task_list:
                task.start()
            time.sleep(sleep_time)
    except Exception as e:
        my_message.ifttt_send_meaasge("程序发生异常%s" % e)


def run():
    init_task_list()
    t = threading.Thread(target=start_task)
    t.start()

