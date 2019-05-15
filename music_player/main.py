import os
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
from pygame import mixer

# initialize root properties
root = Tk()
# root.geometry("500x500")
root.title("MaxXx Music Player")
root.iconbitmap("images/logo.ico")

# use pygame mixer for sound
mixer.init()
song_status = "STOPPED"

song_string = StringVar()
song_string.set("Select a song with File > Open...")
song_label = Label(root, textvariable=song_string)

# create and configure menubar
menubar = Menu(root)
root.config(menu=menubar)


# function for Open... menu item: select a song and load it
def open_file_dialog():
    global song_status

    try:
        file_name = filedialog.askopenfilename()
        mixer.music.load(file_name)
        song_string.set(os.path.basename(file_name))
        song_status = "STOPPED"
        play_button["image"] = play_image
    except Exception as e:
        print(str(e))
        pass


# create File submenu
file_submenu = Menu(menubar, tearoff=False)
menubar.add_cascade(label="File", menu=file_submenu)
file_submenu.add_command(label="Open...", command=open_file_dialog)
file_submenu.add_command(label="Exit", command=root.destroy)


# function for About menu item
def show_about():
    messagebox.showinfo(title="About", message="This was made by Max")


# create Help submenu
help_submenu = Menu(menubar, tearoff=False)
menubar.add_cascade(label="Help", menu=help_submenu)
help_submenu.add_command(label="About", command=show_about)

# create PhotoImages for buttons
play_image = ImageTk.PhotoImage(Image.open("images/play_button.png"))
pause_image = ImageTk.PhotoImage(Image.open("images/pause_button.png"))
stop_image = ImageTk.PhotoImage(Image.open("images/stop_button.png"))
prev_image = ImageTk.PhotoImage(Image.open("images/prev_button.png"))
next_image = ImageTk.PhotoImage(Image.open("images/next_button.png"))


# functions for the buttons
def play():
    global song_status

    try:
        if song_status == "STOPPED":
            mixer.music.play()
            song_status = "PLAYING"
            play_button["image"] = pause_image

        elif song_status == "PLAYING":
            mixer.music.pause()
            song_status = "PAUSED"
            play_button["image"] = play_image

        elif song_status == "PAUSED":
            mixer.music.unpause()
            song_status = "PLAYING"
            play_button["image"] = pause_image
    except Exception as e:
        print(str(e))
        song_string.set("Select a song with File > Open...")
    finally:
        print(f"[DEBUG] Song is now {song_status}")


def stop():
    global song_status

    mixer.music.stop()
    song_status = "STOPPED"
    play_button["image"] = play_image
    print(f"[DEBUG] Song is now {song_status}")


def set_vol(value):
    volume = int(value) / 100
    mixer.music.set_volume(volume)


buttons_frame = Frame(root)

# create button widgets
play_button = Button(buttons_frame, image=play_image, command=play)
stop_button = Button(buttons_frame, image=stop_image, command=stop)

# create volume slider
volume_slider = Scale(
    root, from_=0, to=100, orient=HORIZONTAL, command=set_vol)
volume_slider.set(100)


# pack widgets
play_button.pack(side=LEFT)
stop_button.pack(side=LEFT)
song_label.pack()
buttons_frame.pack()
volume_slider.pack()

root.mainloop()
