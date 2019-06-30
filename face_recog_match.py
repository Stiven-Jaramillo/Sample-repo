import face_recognition

image_of_jim = face_recognition.load_image_file(
    "./face_recognition/img/known/Jim Carrey.jpg"
)
jim_face_encoding = face_recognition.face_encodings(image_of_jim)[0]

unknow_image = face_recognition.load_image_file(
    "face_recognition//img//unknown//Dumb.jpg"
)
unknown_face_encoding = face_recognition.face_encodings(unknow_image)[0]

# compare faces
results = face_recognition.compare_faces([jim_face_encoding], unknown_face_encoding)

if results[0]:
    print("This is Jim Carrey")
else:
    print("This is NOT Jim Carrey")

