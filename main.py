from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from pages import Pages
from threading import Thread,Lock
from Processes.screen import screen
from Processes.utils import getScreenSize
import  time
def utilThread(root:tb.Window,lock):
    global screenWidth,screenHeight
    while True:
        screenWidth,screenHeight = getScreenSize(root)
        time.sleep(1)
if __name__=="__main__":
    screenWidth:int=600
    screenHeight:int = 400
    screenStatus = True
    mainFrame,root = screen()
    lock = Lock()
    Pages.login(mainFrame,screenWidth,screenHeight)
    thread2 = Thread(target=utilThread,args=(root,lock))
    thread2.daemon = True
    thread2.start()
    print(screenWidth)
    root.mainloop()