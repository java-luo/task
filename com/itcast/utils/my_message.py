import requests


# IFTTT提醒
def ifttt_send_meaasge(params, addressee="https://maker.ifttt.com/trigger/request/with/key/FTpKdXF5XOciUIDdUje5s"):
    response = requests.get(addressee, params=params)


# 微信方糖提醒
def wechat_send_meaasge(params,
                        addressee="https://sc.ftqq.com/SCU97534T2bec3e26845aead32d15d549ccdc1eb75eba2795abfd6.send"):
    response = requests.get(addressee, params=params)
