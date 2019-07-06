import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier("cascades//data//haarcascade_frontalface_alt2.xml")

cap = cv2.VideoCapture(0)


while True:
    # Para capturar frame por frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    for (x, y, w, h) in faces:
        print(x, y, w, h)
        # The region of interes it's the square made of h * w
        roi_gray = gray[y : y + h, x : x + w]
        roi_frame = frame[y : y + h, x : x + w]

        # Recognized? deep learning model predict keras, tensorflow, pytorch, scikit learn

        img_item = "my_image.png"
        # Para guardar una imagen en un archivo especificado (nombre y formato,arreglo numpy)
        cv2.imwrite(img_item, roi_gray)

        color = (51, 255, 255)  # BGR 0-255 and this time its blue
        stroke = 2  # How thick ists the line of the rectangle
        end_coord_x = x + w
        end_coord_y = y + h
        cv2.rectangle(frame, (x, y), (end_coord_x, end_coord_y), color, stroke)

    # Para mostrar los frames resultantes
    cv2.imshow("stiv_camera", frame)
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
