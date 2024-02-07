import time

import pyautogui
from pynput import keyboard


class AutoClicker:
    def __init__(self, clicks, interval):
        self.clicks = clicks
        self.interval = interval
        self.running = True
        self.listener = keyboard.Listener(OnRelease=self.on_release)
        self.listener.start()

    def on_release(self, key):
        if key == keyboard.Key.esc:
            self.running = False
            return False

    def start_clicking(self):
        while 1:
            pyautogui.click()
            print('3...')
            time.sleep(self.interval)
            print('2...')
            time.sleep(self.interval)
            print('1...')
            time.sleep(self.interval)
            print('CLICK!')


auto_clicker = AutoClicker(1000000, 0.000001)
auto_clicker.start_clicking()
