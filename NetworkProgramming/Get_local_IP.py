import socket
# 获取本机计算机名称
hostname = socket.gethostname()
# 获取本机ip
ip = socket.gethostbyname(hostname)
print("你的计算机名称为:  " + hostname)
print("你的计算机网络IP为:" + ip)
