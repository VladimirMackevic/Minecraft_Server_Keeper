import time
import win32gui
import win32con
import win32api
import os

def get_cmd(window_title, text):
    # Find CMD window or launch server
    hwnd = win32gui.FindWindow(None, window_title)
    if hwnd == 0:
        print("CMD window not found!")
        os.chdir("C:\Games\Crazy server")
        os.startfile("Run.bat")
        return

    # Typing
    for char in text:
        win32api.SendMessage(hwnd, win32con.WM_CHAR, ord(char), 0)

    # Entering
    win32api.SendMessage(hwnd, win32con.WM_CHAR, 13, 0)


Flag = 0

while Flag == 0:
    time.sleep(20)
    get_cmd("C:\\Windows\\system32\\cmd.exe", "/say Testing")