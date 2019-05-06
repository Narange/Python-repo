import os
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFilter

#initialize root properties
root = Tk()
#root.geometry("500x500")
root.title("Image Manipulator")

#create and configure menubar
menubar = Menu(root)
root.config(menu = menubar)

#global var for file name
file_name = "images/yeah.jpg"


#default image
original_image = Image.open(file_name)
#the working copy to be manipulated
working_image = original_image
#working image PhotoImage - to be applied to image_label
working_image_PH = ImageTk.PhotoImage(working_image)


#function for Open... menu item: select an image and load it
def open_file_dialog():
	global original_image, working_image, file_name, image_label

	file_name = filedialog.askopenfilename()
	original_image = Image.open(file_name)
	working_image = original_image
	image_label["image"] = ImageTk.PhotoImage(working_image)

	print(file_name)


#create File submenu
file_submenu = Menu(menubar, tearoff = False)
menubar.add_cascade(label = "File", menu = file_submenu)
file_submenu.add_command(label = "Open...", command = open_file_dialog)
file_submenu.add_command(label = "Exit", command = root.destroy)

#function for About menu item
def show_about():
	messagebox.showinfo(title = "About", message = "This was made by Max")

#create Help submenu
help_submenu = Menu(menubar, tearoff = False)
menubar.add_cascade(label = "Help", menu = help_submenu)
help_submenu.add_command(label = "About", command = show_about)

#function for apply effect button
def apply_effect():
	global image_label, working_image

	#apply effect to image and update the shown working image
	working_image = working_image.filter.ImageFilter.GaussianBlur(radius = 10)

	#create Tkinter-compatible PhotoImage
	ImageTk.PhotoImage(working_image)

	image_label["image"] = working_image
	print("effect button was clicked")


#frame for image
image_frame = Frame(root)
image_label = Label(image_frame, image = ImageTk.PhotoImage(working_image))

#frame for controls
controls_frame = Frame(root)
effect_button = Button(controls_frame, text = "Apply effect", command = apply_effect)


#pack widgets

#in image_frame
image_label.pack()
image_frame.pack(side = LEFT)

#in controls_frame
effect_button.pack()
controls_frame.pack(side = LEFT)

root.mainloop()