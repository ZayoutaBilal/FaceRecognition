import cv2
import os
import tkinter as tk
from tkinter import simpledialog, messagebox


def take_photo_and_save():
    # Create a folder to save photos if it doesn't exist
    folder_name = "images"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Capture a photo using the default camera (usually the built-in webcam)
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()

    # Release the camera
    cap.release()

    # Destroy any existing Tkinter windows
    root.destroy()

    # Ask for your name using a Tkinter simple dialog
    name = simpledialog.askstring("Input", "Please insert your name:")

    # Save the photo with your name as the filename in the specified folder
    photo_path = os.path.join(folder_name, f"{name}.jpg")
    cv2.imwrite(photo_path, frame)

    # Display an alert with the success message
    messagebox.showinfo("Success", f"Photo saved successfully for {name}")


def capture_photo():
    # Capture a photo when the button is clicked
    take_photo_and_save()


# Create the main Tkinter window
root = tk.Tk()
root.title("Face Saving")

# Create a button to capture the photo
capture_button = tk.Button(root, text="Capture Photo", width=35, command=capture_photo, bg='green')
capture_button.pack(pady=40)

# Start the Tkinter event loop
root.mainloop()
