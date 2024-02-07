import threading
import time

from pynput.keyboard import Key, Listener
from pynput.mouse import Button, Controller

# 创建鼠标控制器
mouse = Controller()

# 默认点击时间间隔和点击的键
default_click_interval = 0.1  # 默认点击时间间隔（秒）
default_click_button = Button.left  # 默认点击的键

# 是否继续点击的标志
clicking = False


def on_press(key):
    global clicking
    if key == Key.ctrl_l:
        # 开始点击
        clicking = True
        click_thread = threading.Thread(target=perform_clicks)
        click_thread.start()
    elif key == Key.esc:
        # 结束点击
        clicking = False


def perform_clicks():
    global clicking
    while clicking:
        mouse.click(default_click_button)
        time.sleep(default_click_interval)


def on_release(key):
    if key == Key.ctrl_l:
        pass  # 如果你想执行一些额外的操作，可以在这里添加
    elif key == Key.esc:
        # 停止点击
        global clicking
        clicking = False
        return False


# 监听键盘事件
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
