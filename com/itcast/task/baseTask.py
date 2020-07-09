from datetime import datetime

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
