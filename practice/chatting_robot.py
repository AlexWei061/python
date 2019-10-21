import requests
import re
key1 = "68b26f6b94f54241b7fa78ca1721192e"              #王重森
key2 = "cb16bc7fc45847a88d2dc70afd70b011"              #冯子曦

while True:
   info = input("\n我:")
   url = "http://www.tuling123.com/openapi/api?key="+key2+"&info="+info
   res = requests.get(url).text
   reg = r'"text":"(.*?)"'
   reg = re.compile(reg,re.S)
   data = re.findall(reg,res)
   print(*data,sep = "\n")
