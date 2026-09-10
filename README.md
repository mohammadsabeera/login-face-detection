# login-face-detection
Python-based biometric login system using Tkinter and OpenCV with real-time face detection through the Haar Cascade algorithm.
# 🔐 Login Face Detection System

## 📌 Project Overview

**Login Face Detection System** is a Python-based biometric authentication project that combines a traditional login system with real-time face detection.

The system first validates the user's username and password. After successful credential verification, it activates the webcam and uses **OpenCV with the Haar Cascade algorithm** to detect a face in real time. When a face is detected, the system displays a successful login message.

## 🎯 Objectives

* Develop a secure login system using face detection
* Reduce dependency on traditional password-based authentication
* Provide fast and real-time authentication
* Prevent unauthorized access through biometric verification
* Create a user-friendly and contactless authentication system

## 🛠️ Technologies Used

| Technology   | Purpose                             |
| ------------ | ----------------------------------- |
| Python       | Core programming                    |
| OpenCV       | Image processing and face detection |
| Haar Cascade | Face detection algorithm            |
| Tkinter      | Graphical User Interface            |
| NumPy        | Data and image processing           |
| Webcam       | Real-time image capture             |

## ⚙️ How the System Works

1. The application starts with a login window.
2. The user enters their username and password.
3. The credentials are validated.
4. If the credentials are incorrect, an error message is displayed.
5. If the credentials are correct, the webcam is activated.
6. OpenCV captures real-time video frames.
7. The frames are converted into grayscale.
8. The Haar Cascade classifier detects faces.
9. A rectangle is displayed around the detected face.
10. When a face is detected, **"Face Login Successful"** is displayed.
11. The camera is then released and the application is closed.

## 🔄 Project Workflow

```text
Start
  ↓
Login Window
  ↓
Enter Username & Password
  ↓
Validate Credentials
  ↓
 ┌───────────────┐
 │ Valid Login?  │
 └───────┬───────┘
      No ↓       ↓ Yes
   Error      Activate Webcam
               ↓
          Capture Frames
               ↓
         Convert to Grayscale
               ↓
        Haar Cascade Detection
               ↓
         Face Detected?
          ↓ Yes       ↓ No
   Login Successful   Continue
          ↓
      Release Camera
          ↓
          End
```

## 💻 Main Features

* 🔑 Username and password authentication
* 📷 Real-time webcam access
* 👤 Face detection
* 🖥️ Tkinter graphical interface
* ⚡ Real-time verification
* ❌ Invalid login detection
* ✅ Face login success notification

## 📂 Project Structure

```text
Login-Face-Detection/
│
├── login_face_detection.py
├── README.md
├── requirements.txt
└── screenshots/
    ├── login.png
    └── face_detection.png
```

## 📦 Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

### 2. Open the project folder

```bash
cd Login-Face-Detection
```

### 3. Install required libraries

```bash
pip install opencv-python numpy
```

Tkinter is generally included with standard Python installations on Windows.

### 4. Run the application

```bash
python login_face_detection.py
```

## 🔑 Demo Login

For the current demonstration version:

```text
Username: admin
Password: 1234
```

> ⚠️ These credentials are included only for demonstration purposes. A production authentication system should not store passwords directly in source code.

## 📸 Project Screenshots

Add screenshots of:

* Login screen
* Webcam face detection screen
* Face Login Successful message

## 🔒 Security & Privacy

The project demonstrates biometric authentication and can be further enhanced with:

* End-to-end encryption
* Secure storage of facial data
* Anti-spoofing techniques
* Deep-learning-based face recognition
* Stronger authentication mechanisms
* User consent and privacy controls

## 🚀 Future Enhancements

* Implement actual face recognition instead of only face detection
* Add a secure database for registered users
* Implement deep-learning-based facial recognition
* Add anti-spoofing protection
* Add encrypted biometric data storage
* Improve authentication accuracy
* Develop a web or mobile version

## 🎓 Learning Outcomes

Through this project, I gained practical experience in:

* Python programming
* OpenCV
* Computer Vision
* Haar Cascade face detection
* Tkinter GUI development
* Webcam-based image processing
* Biometric authentication concepts
* Security and privacy considerations

## 👩‍💻 Author

**Mohammad Sabeera**

B.Tech – Computer Science & Engineering (Data Science)

## ⭐ Project

If you find this project useful, consider giving the repository a ⭐.
