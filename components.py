from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *
class Components:
    @staticmethod
    def Label(main:Frame,text:str,font_size:int=24,font_family:str="Helvetica",pady:int=10)->None:
        """Takes the main frame and text as parameter and add them to the Window"""
        home_label:Label = tb.Label(main,text=text,font=(font_family,font_size))
        home_label.pack(pady=pady)