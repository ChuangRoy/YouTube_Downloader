import tkinter as tk
import tkinter.ttk as ttk
import threading
import time
from PIL import Image, ImageTk

class GUI:
    videos=[]
    def __init__ (self):
        self.root = tk.Tk() ## Root
        ## Make Window be center of the screen
        self.screenwidth = self.root.winfo_screenwidth()
        self.screenheight = self.root.winfo_screenheight()
        self.width = 600
        self.height = 800
        self.download_video_index = 0
        self.x = int(self.screenwidth / 2 - self.width / 2)
        self.y = int(self.screenheight / 2 - self.height / 2)
        ## Create Window
        self.create_window()
        ## Mainloop
        threading.Thread(target=GUI.mainloop(self.root))

    def create_window (self):
        try:
            ## Fix the diaplay Windows platform
            from ctypes import windll

            windll.shcore.SetProcessDpiAwareness(1)
        finally:
            ## Window settings
            self.root.title("YouTube Downloader Start From Scratch")
            self.root.geometry(f"{self.width}x{self.height}+{self.x}+{self.y}") # width x height + x + y
            self.root.resizable(False, False)

            ## Create text
            self.ytdl_text = tk.Label(self.root, text="YouTube Downloader", font="Consolas 18 bold")
            self.ytdl_text.pack(pady=5)

            ## Youtube image
            with Image.open("../resources/youtube_PNG14.png") as self.yt_img:
                self.yt_img.thumbnail((200, 200))
                self.yt_img = ImageTk.PhotoImage(self.yt_img)
                self.yt_image = tk.Label(self.root, image=self.yt_img)
                self.yt_image.place(rely=0.2, relx=0.5, anchor="center")

            ## Create input box
            self.dl_url = tk.StringVar()
            self.dl_inputbox = ttk.Entry(self.root, textvariable=self.dl_url,
                    width=48, font="Consolas 14 normal")
            self.dl_inputbox.place(rely=0.35, relx=0.41, anchor='center')
            # entry.focus()

            ## Create download button
            self.download_btn = tk.Button(self.root, text="Download",
                    command=self.download(self.download_video_index),
                        bg="orange", fg="black", font="Consolas 12 bold",
                            relief="solid")
            self.download_btn.place(rely=0.35, relx=0.9, anchor='center')

            ## Downloaded video Listbox
            self.dl_lstbox = tk.Listbox(self.root, width=80, height=27,
                    selectmode="extened")
            self.dl_lstbox.place(rely=0.4, relx=0.5, anchor="n")

    def download(self, index):
        ## TODO:Download video
        print(f"Download video from {self.dl_url.get()}")
        index += 1 self.videos.append(f"{self.dl_url.get()}") # Video name 
        self.dl_lstbox.insert(END, "dl video")


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
    gui = GUI()
