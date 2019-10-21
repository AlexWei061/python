import easygui
while True:
    title=easygui.enterbox('请输入您要进行的运算(四则运算)')
    if title.find('+') != -1:
        num1=easygui.enterbox('请输入第一个加数')
        num2=easygui.enterbox('请输入第二个加数')
        easygui.msgbox(float(num1)+float(num2))
        break
    elif title.find('-') != -1:
        num3=easygui.enterbox('请输入被减数')
        num4=easygui.enterbox('请输入减数')
        easygui.msgbox(float(num3)-float(num4))
        break
    elif title.find('*') != -1:
        num5=easygui.enterbox('请输入第一个乘数')
        num6=easygui.enterbox('请输入第二个乘数')
        easygui.msgbox(float(num5)*float(num6))
        break
    elif title.find('/') != -1:
        num7=easygui.enterbox('请输入被除数')
        num8=easygui.enterbox('请输入除数')
        easygui.msgbox(float(num7)/float(num8))
        break
    else:
        easygui.msgbox('请输入正确的四则运算!')
