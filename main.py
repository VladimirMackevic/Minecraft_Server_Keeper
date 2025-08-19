import time
import win32gui
import win32con
import win32api
import os
import socket
import ctypes

# Windows API flags to prevent sleep
ES_CONTINUOUS       = 0x80000000
ES_SYSTEM_REQUIRED  = 0x00000001
ES_AWAYMODE_REQUIRED = 0x00000040

def prevent_sleep():
    # Keeps PC running
    ctypes.windll.kernel32.SetThreadExecutionState(
        ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_AWAYMODE_REQUIRED
    )

def server_check(host="localhost", port=25565):
    # Ping server
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((host, port))
    except (socket.timeout, ConnectionRefusedError):
        return False
    else:
        sock.close()
        return True

def get_cmd(window_title, text):
    # Find CMD window or launch server
    hwnd = win32gui.FindWindow(None, window_title)
    if hwnd == 0:
        print("CMD window not found!")
        os.chdir("C:\Games\Crazy server")
        os.startfile("Run.bat")
        return

    time.sleep(595) # Checking timer
    if server_check():
        return
    else:
        # Press enter
        win32api.SendMessage(hwnd, win32con.WM_CHAR, 13, 0)
        print("Attempting to press any key...")

#Dummy loop and flavour testing text
Flag = 0

prevent_sleep()
while Flag == 0:
    time.sleep(5) # Safety timer
    get_cmd("C:\\Windows\\system32\\cmd.exe", "/say Testing")