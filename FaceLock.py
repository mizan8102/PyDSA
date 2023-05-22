import cv2
import face_recognition
import pickle

# Load the known faces and embeddings
with open("known_faces.pkl", "rb") as f:
    known_faces = pickle.load(f)
    known_names = pickle.load(f)

# Initialize the video stream and pointer to output video file
video_capture = cv2.VideoCapture(0)

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = frame[:, :, ::-1]

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Loop through each face in this frame of video
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_faces, face_encoding)

        # If a match was found in known_faces, just use the first one.
        if True in matches:
            first_match_index = matches.index(True)
            name = known_names[first_match_index]
            print(f"Access granted for {name}")
            # Perform some action to unlock the computer or perform some other task
        else:
            print("Access denied")
            # Keep the computer locked
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video stream pointer
video_capture.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
