import threading
import ctypes
from playsound import playsound
import time
import os
import sys

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def play():
    playsound(resource_path('TheFatRat-XeogenesisOutroPart.mp3'))

def countandlock():
    time.sleep(2)
    print("Locking in 5...")
    time.sleep(3)
    print("4...")
    time.sleep(3)
    print("3...")
    time.sleep(3)
    print("2...")
    time.sleep(3)
    print("1..!")
    time.sleep(2)
    ctypes.windll.user32.LockWorkStation()


x = threading.Thread(target=play)
x.start()
x = threading.Thread(target=countandlock)
x.start()