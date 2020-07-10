from flask import Blueprint, request

from com.itcast.service import TaskService
from com.itcast.utils import ServerResponse

task = Blueprint("task", __name__)


@task.route("/getTaskList")
def get_task_list():
    return TaskService.get_task_list()


@task.route("/removeTask")
def remove_task():
    taskName = request.args.get("taskName")
    return TaskService.remove_task(taskName)


@task.route("/createGuoboRob", methods=['POST'])
def create_guobo_rob():
    name = request.form.get("taskName")
    kw = request.form.get("kw")
    if name == '' or name == None:
        return ServerResponse.createError(msg="任务名称不能为空哦!")
    return TaskService.create_guobo_rob(name, kw)


@task.route("/createGuoboMonitor", methods=['POST'])
def create_guobo_monitor():
    name = request.form.get("taskName")
    kw = request.form.get("kw")
    if name == '' or name == None:
        return ServerResponse.createError(msg="任务名称不能为空哦!")
    return TaskService.create_guobo_monitor(name, kw)
