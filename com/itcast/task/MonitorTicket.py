from com.itcast.splider import Guobo_Spider
from com.itcast.task.baseTask import baseTask


class MonitorTicket(baseTask):

    def run(self):
        Guobo_Spider.start()

