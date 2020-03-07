# 使用微信接口给微信好友发送消息，
import itchat
import time

# 自动登录方法，hotReload=True可以缓存，不用每次都登录,但是第一次执行时会出现一个二维码，需要手机微信扫码登录
itchat.auto_login(hotReload=True)

# 搜索好友，search_friends("xxx"),其中"xxx"为好友昵称，备注或微信号不行
userfinfo = itchat.search_friends("徐质文")   # "智能群管家014"为好友昵称

# print(userfinfo)，获取userinfo中的UserName参数
userid = userfinfo[0]["UserName"]   # 获取用户id

# 调用微信接口发送消息
# itchat.send("hello dear", userid)  # 通过用户id发送信息
# 或
# itchat.send_msg(msg='hello dear', toUserName=userid)

n = 250

for i in range(0, n):
    # 从8:00到22:00发送
    itchat.send("有毒啊!!!!!!!!!!!!!!!!!!!!!!!!!!!!" + str(i),userid)
    print("send mag succesfully")
    print(time.asctime(time.localtime(time.time())))