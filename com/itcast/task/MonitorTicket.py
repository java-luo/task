from com.itcast.splider import Guobo_Spider
from com.itcast.task.baseTask import baseTask
from com.itcast.utils import Const


class MonitorTicket(baseTask):

    def run(self):
        isOk = Guobo_Spider.start()
        if (not isOk):
            Const.task_list.remove(self)
