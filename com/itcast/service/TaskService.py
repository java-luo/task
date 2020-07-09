from com.itcast.task.GuoBoRobTicket import RobTicket
from com.itcast.utils import Const, ServerResponse


def get_task_list():
    task_list = []
    result_dict = {}
    for task in Const.task_list:
        task_tmp = {}
        task_tmp['taskName'] = task.name
        task_tmp['statTime'] = task.getCreateTime()
        task_tmp['executeTime'] = task.executeTime()
        task_list.append(task_tmp)
    result_dict['result_tast'] = task_list
    return result_dict


def get_taskName_list():
    taskName_list = []
    for task in Const.task_list:
        taskName_list.append(task.name)
    return taskName_list


def remove_task(taskName):
    result = {}
    for task in Const.task_list:
        if task.name == taskName:
            Const.task_list.remove(task)
            return ServerResponse.createSuccess()
    return ServerResponse.createError()


def create_guobo_rob(name, kw):
    taskName_list=get_taskName_list()
    if name in taskName_list:
        return ServerResponse.createError("任务名称不能重复,请重新命名")
    rob = RobTicket(name, kw)
    Const.task_list.append(rob)
    return ServerResponse.createSuccess()

