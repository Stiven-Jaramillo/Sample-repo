import face_recognition
from PIL import Image, ImageDraw

image_of_jona = face_recognition.load_image_file(
    "./face_recognition/img/known/Jona Kahnwald.png"
)
jona_face_encoding = face_recognition.face_encodings(image_of_jona)[0]

image_of_hannah = face_recognition.load_image_file(
    "./face_recognition/img/known/Hannah Kahnwald.png"
)
hannah_face_encoding = face_recognition.face_encodings(image_of_hannah)[0]

image_of_katharina = face_recognition.load_image_file(
    "./face_recognition/img/known/Katharina Nielsen.png"
)
katharina_face_encoding = face_recognition.face_encodings(image_of_katharina)[0]

image_of_mark = face_recognition.load_image_file(
    "./face_recognition/img/known/Mark Waschke.jpg"
)
mark_face_encoding = face_recognition.face_encodings(image_of_mark)[0]

#  Create arrays of encodings and names
known_face_encodings = [
    jona_face_encoding,
    hannah_face_encoding,
    katharina_face_encoding,
    mark_face_encoding,
]

known_face_names = [
    "Jona Kahnwald",
    "Hannah Kahnwald",
    "Katharina Nielsen",
    "Mark Waschke",
]

# Load test image to find faces in
test_image = face_recognition.load_image_file(
    "./face_recognition/img/groups/darl_cast.png"
)

# Find faces in test image
face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)

# Convert to PIL format
pil_image = Image.fromarray(test_image)

# Create a ImageDraw instance
draw = ImageDraw.Draw(pil_image)

# Loop through faces in test image
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

    name = "Unknown Person"

    # If match
    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]

    # Draw box
    draw.rectangle(((left, top), (right, bottom)), outline=(255, 255, 0))

    # Draw label
    text_width, text_height = draw.textsize(name)
    draw.rectangle(
        ((left, bottom - text_height - 10), (right, bottom)),
        fill=(255, 255, 0),
        outline=(255, 255, 0),
    )
    draw.text((left + 6, bottom - text_height - 5), name, fill=(0, 0, 0))

del draw

# Display image
pil_image.show()

# Save image
pil_image.save("identify.jpg")

