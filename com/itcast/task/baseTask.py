from datetime import datetime
from com.itcast.utils import Const,my_message
class baseTask(object):
    def __init__(self, name, kw=None):
        self.name = name
        self.start_time = datetime.now()
        self.kw=kw

    def executeTime(self):
        execute_time = datetime.now() - self.start_time;
        execute_time = str(execute_time)
        execute_time = execute_time.split('.')[0]
        return execute_time

    def getCreateTime(self):
        return self.start_time.strftime("%Y-%m-%d %H:%M:%S")

    def run(self):
        pass

    def start(self):
        try:
            self.run()
        except Exception as e:
            msg="任务:%s中止 异常原因%s" %(self.name,e)
            my_message.ifttt_send_meaasge({"value1":msg})
            print(msg)
            Const.task_list.remove(self)

