from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFilter, ImageOps

# initialize root properties
root = Tk()
root.title("Image Manipulator")

# create and configure menubar
menubar = Menu(root)
root.config(menu=menubar)

# global var for file name - set a default one for now
file_name = "images/yeah.jpg"

# default image
original_image = Image.open(file_name)

# the working copy to be manipulated
working_image = original_image

# working image PhotoImage - to be applied to image_label
working_image_PH = ImageTk.PhotoImage(working_image)


# function for Open... menu item: select an image and load it
def open_file_dialog():
    global original_image, working_image, file_name, image_label, working_image_PH

    file_name = filedialog.askopenfilename()
    original_image = Image.open(file_name)
    working_image = original_image

    # The next two lines must be seperate
    # PhotoImage must be rendered and assigned before use
    working_image_PH = ImageTk.PhotoImage(working_image)
    image_label["image"] = working_image_PH

    print(file_name)


# create File submenu
file_submenu = Menu(menubar, tearoff=False)
menubar.add_cascade(label="File", menu=file_submenu)
file_submenu.add_command(label="Open...", command=open_file_dialog)
file_submenu.add_command(label="Exit", command=root.destroy)


# function for About menu item
def show_about():
    messagebox.showinfo(title="About", message="This was made by Nicolas")


# create Help submenu
help_submenu = Menu(menubar, tearoff=False)
menubar.add_cascade(label="Help", menu=help_submenu)
help_submenu.add_command(label="About", command=show_about)


# reset the image to original
def reset_image():
    global original_image, working_image, working_image_PH

    working_image = original_image
    working_image_PH = ImageTk.PhotoImage(working_image)
    image_label["image"] = working_image_PH


# effect: Gaussian blur
def apply_effect_blur():
    global image_label, working_image, working_image_PH

    try:
        # get the user input intensity
        input_radius = int(blur_entry.get())

        # apply effect to image and update the working image with blur
        new_image = working_image
        working_image = new_image.filter(ImageFilter.GaussianBlur(radius=input_radius))

        # create PhotoImage and apply it to the Label
        working_image_PH = ImageTk.PhotoImage(working_image)
        image_label["image"] = working_image_PH
        print(f"[DEBUG] Blur button was clicked, with radius {input_radius}")
    except ValueError as e:
        print(str(e))
        messagebox.showerror(title="Invalid value", message="An integer must be entered for blur radius")


# effect: flip horizontally
def apply_effect_flip_H():
    global working_image, working_image_PH

    new_image = working_image
    working_image = ImageOps.mirror(new_image)

    working_image_PH = ImageTk.PhotoImage(working_image)
    image_label["image"] = working_image_PH


# effect: flip vertically
def apply_effect_flip_V():
    global working_image, working_image_PH

    new_image = working_image
    working_image = ImageOps.flip(new_image)

    working_image_PH = ImageTk.PhotoImage(working_image)
    image_label["image"] = working_image_PH


# effect: invert image colors
def apply_effect_invert():
    global working_image, working_image_PH

    new_image = working_image
    working_image = ImageOps.invert(new_image)

    working_image_PH = ImageTk.PhotoImage(working_image)
    image_label["image"] = working_image_PH


# effect: posterize image
def apply_effect_posterize():
    global working_image, working_image_PH

    new_image = working_image
    working_image = ImageOps.posterize(new_image, 1)

    working_image_PH = ImageTk.PhotoImage(working_image)
    image_label["image"] = working_image_PH


# frame for image
image_frame = Frame(root)
image_label = Label(image_frame, image=working_image_PH)


# frame for controls
controls_frame = Frame(root)

# reset button
reset_button = Button(controls_frame, text="Reset image", command=reset_image, padx=3)

# entry field for blur effect
blur_label = Label(controls_frame, text="Blur radius:")
blur_entry = Entry(controls_frame, width=8)
# button for blur effect
blur_button = Button(controls_frame, text="Blur", command=apply_effect_blur, padx=3)

# button for flip Horizontal/Vertical effects
flip_H_button = Button(controls_frame, text="Flip horizontally", command=apply_effect_flip_H, padx=3)
flip_V_button = Button(controls_frame, text="Flip vertically", command=apply_effect_flip_V, padx=3)

# buttons for invert and posterize
invert_button = Button(controls_frame, text="Invert", command=apply_effect_invert, padx=3)
posterize_button = Button(controls_frame, text="Posterize", command=apply_effect_posterize, padx=3)


# pack widgets

# in image_frame
image_label.pack()
image_frame.pack(side=LEFT)

# in controls_frame
reset_button.pack()
blur_label.pack(pady=(10, 0))
blur_entry.pack()
blur_button.pack()
flip_H_button.pack(pady=(10, 0))
flip_V_button.pack()
invert_button.pack(pady=(10, 0))
posterize_button.pack()
controls_frame.pack(side=LEFT)

root.mainloop()
