from PIL import Image

im = Image.open("./face_recognition/img/groups/team2.jpg")

x1 = 0
y1 = 0
x2 = im.width
y2 = im.height
cropped_im = im.crop((x1, y1, x2, y2))
cropped_im.show()

