import cv2
import dlib
import face_recognition
from tkinter import Tk, Label, Button, Canvas, Frame, messagebox, simpledialog
from PIL import Image, ImageTk
import os

# Load the pre-trained face detection model from Dlib
detector = dlib.get_frontal_face_detector()

# Initialize face recognition
known_faces = []
known_usernames = []


def capture_video():
    ret, frame = cap.read()

    if ret:
        # Convert the frame to RGB for face recognition
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect faces in the frame
        faces = detector(frame)

        # Reset the count to 0
        num_faces = 0

        for face in faces:
            # Draw a green rectangle around the detected face
            top, right, bottom, left = face.top(), face.right(), face.bottom(), face.left()
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

            # Increment the count for each detected face
            num_faces += 1

        # Display the number of detected faces outside the loop
        status_label.config(text=f"Number of Persons: {num_faces}")

        # Convert the frame to RGB for display in Tkinter
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(img)
        canvas.img = img
        canvas.create_image(0, 0, anchor='nw', image=img)

    # Schedule the function to be called again after 10 milliseconds
    root.after(10, capture_video)



# Open the camera (0 represents the default camera)
cap = cv2.VideoCapture(0)

# GUI setup
root = Tk()
root.title("Face Recognition GUI")

# Left Frame (Buttons)
left_frame = Frame(root)
left_frame.pack(side='left', padx=10)

exit_button = Button(left_frame, text="Exit", command=root.destroy, width=20, height=1, bg="red")
exit_button.pack(pady=10)

# Right Frame (Camera Feed)
right_frame = Frame(root)
right_frame.pack(side='right')

canvas = Canvas(right_frame, width=640, height=480)
canvas.pack()

# Status Label
status_label = Label(root, text="Number of Persons: 0")
status_label.pack()

# Start capturing the video feed
capture_video()

# Run the Tkinter main loop
root.mainloop()

# Release the camera and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
