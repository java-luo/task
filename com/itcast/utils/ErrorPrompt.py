from com.itcast.utils import my_message


# 错误提示装饰器, 会把错误发送到IFTTT上
def error_send_msg(actual_do):
    def add_robust(*args, **keyargs):
        try:
            return actual_do(*args, **keyargs)
        except Exception as  e:
            errorMsg = '程序执行错误: %s方法:%s' % (actual_do.__name__, e)
            # print(errorMsg)
            # my_message.ifttt_send_meaasge({"value1": errorMsg})

    return add_robust

