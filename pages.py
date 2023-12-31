from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from Pages.login import login
from Pages.userPage import userPage
from Pages.homePage import homePage
# global Valuess
class Pages:
    def __init__(self,main:Frame):
        self.main:Frame = main
    @staticmethod
    def login(main,widht:int,height:int):
        global Name,Dept,Roll,screenWidht,screenHeight
        screenWidht= widht
        screenHeight= height
        Name,Dept,Roll  = login(main,Navigator,widht,height)
    @staticmethod 
    def userPage(main,l1):
        userPage(main,Navigator,Name,Dept,Roll,Equipment,Hours,l1)
    @staticmethod 
    def homePage(main,screenWidht,screenHeight):
        global Equipment,Hours
        Equipment,Hours = homePage(main,screenWidht,Navigator,screenHeight)
class Navigator:
    @staticmethod
    def clear(frame):
        for widgets in frame.winfo_children():
            widgets.destroy()
    @staticmethod
    def navigate(url:str,frame,l1=[]):
        """Navigate to a new route"""
        Navigator.clear(frame)
        match url:
            case "login":
                Pages.login(frame,screenWidht,screenHeight)
            case "userPage":
                Pages.userPage(frame,l1)
            case "home":
                Pages.homePage(frame,screenWidht,screenHeight)
