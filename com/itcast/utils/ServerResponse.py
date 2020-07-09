def createSuccess(code=0, msg="成功", data={}):
    return {"code": code, "msg": msg, "data": data}


def createError(code=1, msg="失败"):
    return {"code": code, "msg": msg}
