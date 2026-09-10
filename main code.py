# ============================================================
# LOGIN FACE DETECTION SYSTEM
# Technologies: Python, OpenCV, Tkinter, NumPy
# ============================================================

import cv2
import tkinter as tk
from tkinter import messagebox


# ============================================================
# LOGIN DETAILS
# ============================================================

USERNAME = "admin"
PASSWORD = "1234"


# ============================================================
# FACE DETECTION FUNCTION
# ============================================================

def start_face_login():

    # Load Haar Cascade face detector
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades +
        "haarcascade_frontalface_default.xml"
    )

    # Open webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        messagebox.showerror(
            "Camera Error",
            "Unable to access the webcam."
        )
        return

    print("Show your face to login...")

    while True:

        # Capture frame
        ret, frame = cap.read()

        if not ret:
            messagebox.showerror(
                "Camera Error",
                "Unable to capture video."
            )
            break

        # Convert frame to grayscale
        gray = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2GRAY
        )

        # Detect faces
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.3,
            minNeighbors=5
        )

        # Draw rectangle around detected face
        for (x, y, w, h) in faces:

            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (255, 0, 0),
                2
            )

            cv2.putText(
                frame,
                "Face Detected",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 0, 0),
                2
            )

        # Display webcam
        cv2.imshow(
            "Face Login",
            frame
        )

        # If face detected
        if len(faces) > 0:

            messagebox.showinfo(
                "Login Successful",
                "Face Login Successful!"
            )

            break

        # Press ESC to exit
        if cv2.waitKey(1) & 0xFF == 27:
            break

    # Release camera
    cap.release()

    # Close OpenCV windows
    cv2.destroyAllWindows()


# ============================================================
# LOGIN FUNCTION
# ============================================================

def login():

    user = username_entry.get()
    pwd = password_entry.get()

    if user == USERNAME and pwd == PASSWORD:

        messagebox.showinfo(
            "Login",
            "Password Verified!"
        )

        # Hide login window
        root.withdraw()

        # Start face detection
        start_face_login()

        # Close application
        root.destroy()

    else:

        messagebox.showerror(
            "Login Error",
            "Invalid Username or Password!"
        )


# ============================================================
# GUI LOGIN WINDOW
# ============================================================

root = tk.Tk()

root.title("Login Face Detection System")
root.geometry("350x250")
root.resizable(False, False)


# Title
title_label = tk.Label(
    root,
    text="LOGIN SYSTEM",
    font=("Arial", 18, "bold")
)

title_label.pack(pady=15)


# Username
username_label = tk.Label(
    root,
    text="Username",
    font=("Arial", 11)
)

username_label.pack()

username_entry = tk.Entry(
    root,
    width=30
)

username_entry.pack(pady=5)


# Password
password_label = tk.Label(
    root,
    text="Password",
    font=("Arial", 11)
)

password_label.pack()

password_entry = tk.Entry(
    root,
    width=30,
    show="*"
)

password_entry.pack(pady=5)


# Login button
login_button = tk.Button(
    root,
    text="LOGIN",
    width=15,
    command=login
)

login_button.pack(pady=20)


# Start application
root.mainloop()