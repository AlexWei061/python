import time

print (time.time())
print (time.localtime( time.time() ))
print (type(int(time.asctime( time.localtime(time.time()) )[11] + time.asctime( time.localtime(time.time()) )[12])))