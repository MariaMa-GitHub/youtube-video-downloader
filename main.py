# YOUTUBE VIDEO DOWNLOADER
from tkinter import *
from pytube import YouTube
from tkinter.messagebox import showinfo
import webbrowser

# program settings
PROGRAM_NAME = "YouTube Video Downloader"
BG_COLOR = "#A9A9A9"
WINDOW_SIZE = "382x275"


# program class
class Program:

    # initialize settings
    def __init__(self):

        self.window = Tk()
        self.window.title(PROGRAM_NAME)
        self.window.config(padx=50, pady=50, bg=BG_COLOR)
        self.window.geometry(WINDOW_SIZE)
        self.window.resizable(width=0, height=0)

        self.title_label = Label(text=PROGRAM_NAME, font=("Arial", 16, "bold"), bg=BG_COLOR, justify="center")
        self.title_label.grid(row=0, column=0, columnspan=2, sticky='we')

        self.instruction_label = Label(text="Link:", bg="white", font=("Arial", 16, "normal"), justify=LEFT)
        self.instruction_label.grid(row=1, column=0, pady=(20, 10), sticky='we')

        self.link_textbox = Entry(font=("Arial", 12, "normal"), bd=5, relief=FLAT)
        self.link_textbox.grid(row=1, column=1, pady=(20, 10), sticky='we')
        self.link_textbox.focus()

        self.name_label = Label(text="File:", bg="white", font=("Arial", 16, "normal"), justify=LEFT)
        self.name_label.grid(row=2, column=0, sticky='we')

        self.name_textbox = Entry(font=("Arial", 12, "normal"), bd=5, relief=FLAT)
        self.name_textbox.grid(row=2, column=1, sticky='we')

        self.download_button = Button(text=" DOWNLOAD AND VIEW ", font=("Arial", 12, "bold"), command=self.download_video)
        self.download_button.grid(row=3, column=0, columnspan=2, pady=(15, 0), sticky='we')

        self.window.mainloop()

    # download video
    def download_video(self):

        try:

            yt = YouTube(self.link_textbox.get())

            mp4files = yt.streams.filter(progressive=True, file_extension='mp4')

            if self.name_textbox.get().strip() == "":
                name = "Video.mp4"
            else:
                name = self.name_textbox.get() + ".mp4"

            mp4files.first().download(filename=name)

            webbrowser.open(name)

        except:

            showinfo(title="ERROR", message="An error occurred. Please try again.")

        self.link_textbox.delete(0, END)
        self.name_textbox.delete(0, END)
        self.link_textbox.focus()


# main program
program = Program()
