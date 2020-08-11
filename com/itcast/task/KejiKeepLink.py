from com.itcast.splider import keji_spider
from com.itcast.task.baseTask import baseTask


class KeepLinkTicket(baseTask):

    def run(self):
        keji_spider.keep_link()

