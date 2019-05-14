from PIL import Image
import os

dir_name = "images"
size_300 = (300, 300)


def create_thumbnails():
    for file in os.listdir(dir_name):
        if file.endswith(".jpg"):
            i = Image.open(dir_name + "/" + file)
            file_name, file_ext = os.path.splitext(file)

            i.thumbnail(size_300)
            i.save(f"300/{file_name}_300{file_ext}")


def rotate_a_lot(file):

    file_name, file_ext = os.path.splitext(file)
    image = Image.open(file)

    # rotate it, once for every degree
    for i in range(360):
        image.rotate(i).save("rotated/rotated_image{}{}".format(i, file_ext))
    for i in range(30):
        image.rotate(i * 12).save(f"rotatedfast/rotated_image{i}{file_ext}")


rotate_a_lot("images/nostrils.jpg")
