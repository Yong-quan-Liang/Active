import win32api
import win32con
import time
import pyautogui as pag
def acquire_coordinate():   #判断鼠标在240内有没有坐标移动
    a,b=pag.position()  #返回鼠标坐标
    print(a,b)
    time.sleep(150)
    c,d=pag.position()
    print(c,d)
    if a==c:
        return 1

def click(x, y):    #点击鼠标
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


def keep_active():      #移动鼠标
    click(10, 10)
    print('点击10')
    time.sleep(0.1)
    print('延时0.1')
    click(100, 100)
    print("点击100")
    time.sleep(2) #延迟单位为秒
    print('移动')

while True:
    g=acquire_coordinate()
    if g==1:
        keep_active()
