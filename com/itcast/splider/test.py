import requests
from com.itcast.utils.SpiderUtil import get_user_agent
proxies={
    "http":"http://165.225.210.83:10605"
}
headers={
    "User-Agent":get_user_agent()
}
r=requests.get("http://91porn.com/index.php",headers=headers,proxies=proxies,timeout=10)
print(r.text)