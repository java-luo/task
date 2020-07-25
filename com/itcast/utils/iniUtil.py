import configparser
from com.itcast.utils.PathUtil import *
rootPath=getRootPath()
config = configparser.ConfigParser()
# -read读取ini文件
print(rootPath)
config.read('./config.ini', encoding='GB18030')


# 输入分组和key值 返回value
def getInI(section, option):
    return config.get(section, option)


print(getInI("spider", "get_ticket_num_url"))