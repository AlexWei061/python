import requests
import re
key1 = "68b26f6b94f54241b7fa78ca1721192e"              #王重森
key2 = "cb16bc7fc45847a88d2dc70afd70b011"              #冯子曦

# 这个程序暂时不能用了,因为tuling123机器人的url新用来一种加密方式加密原始信息,我暂时也不知道加密方式。

while True:
   info = input("\n我:")
   url = "http://www.tuling123.com/openapi/api?key="+key2+"&info="+info
   res = requests.get(url).text
   reg = r'"text":"(.*?)"'
   reg = re.compile(reg,re.S)
   data = re.findall(reg,res)
   print(*data,sep = "\n")
