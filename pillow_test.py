from PIL import Image


# im = Image.open("./face_recognition/img/groups/team2.jpg")
image_name = "./face_recognition/img/groups/team1.jpg"
im = Image.open(image_name)

cropped_im = im.crop((349, 39, 411, 101))
cropped_im.show()

