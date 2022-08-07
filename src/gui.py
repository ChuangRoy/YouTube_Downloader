from tkinter import *
import tkinter as tk
from tkinter.ttk import *
import tkinter.ttk as ttk
import threading
import time

class GUI:
    buttons = []
    texts = []
    def __init__ (self, tk, ttk, time):
        self.tk = tk
        self.ttk = ttk
        self.root = tk.Tk()
        self.time = time
        self.screenwidth = self.root.winfo_screenwidth()
        self.screenheight = self.root.winfo_screenheight()
        self.width = 600
        self.height = 800
        self.x = int(self.screenwidth / 2 - self.width / 2)
        self.y = int(self.screenheight / 2 - self.height / 2)
        self.create_window()
        print("Create a gui window")

    def create_btn_object (self, btntype, width, height):
        # create a button object
        if btntype == 'dlbtn': # download button
            pass
            # button clicked func = download video

    def create_window (self):
        try:
            from ctypes import windll

            windll.shcore.SetProcessDpiAwareness(1)
        finally:
            self.root.title("YouTube Downloader Start From Scratch")
            self.root.geometry(f"{self.width}x{self.height}+{self.x}+{self.y}") # widthxheight+x+y
            self.root.resizable(False, False)
            self.create_text_object("Youtube Downloader")
            threading.Thread(target=GUI.mainloop(self.root))

    def create_text_object (self, txt):
        text = self.tk.Label(self.root, text=txt)
        text.pack()
        self.texts.append(text)

    @staticmethod
    def mainloop (root):
        root.mainloop()
        # while 1:
        #     root.update_idletasks()
        #     root.update()
        #     time.sleep(0.01)

if __name__ == "__main__":
    # root = tk.Tk()
    # threading.Thread(target=GUI.mainloop(root))
    gui = GUI(tk, ttk, time)
    print("It is working.")
