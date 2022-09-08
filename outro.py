import threading
import ctypes
from playsound import playsound
import time

def play():
    playsound('TheFatRat-XeogenesisOutroPart.mp3')

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