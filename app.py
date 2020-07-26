from flask import Flask, render_template,redirect

from com.itcast.controller.GuoboController import guobo
from com.itcast.controller.TaskController import task
from com.itcast.controller.wxController import wx
from com.itcast.task import InitTask

app = Flask(__name__, static_url_path="")
app.register_blueprint(guobo)
app.register_blueprint(task)
app.register_blueprint(wx)

InitTask.run()


@app.route('/')
def hello_world():
    return redirect("/getTicket.html")


# 404接受页面
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


# 404接受页面
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0")
