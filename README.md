# Remote Control of Mobile Screen Projection and Control on PC/Laptop

## Overview
For more information, visit [Prototype Video Demo]([https://youtu.be/CAHjdSgKo1Y](https://www.youtube.com/watch?v=JTCI_KNyddM&feature=youtu.be)).

This project provides a solution for controlling an Android mobile device from a PC/Laptop using Python. It includes features like screen mirroring, navigation, music, and call functionality. The connection between the PC and mobile can be through USB or WiFi.

![Screenshot 2024-07-11 093512](https://github.com/sumionochi/Android-Screen-Automation-Control-using-ABD/assets/89721628/d254bba9-26f8-4136-82d9-0d2ff030df8e)

## Features

- **Screen Mirroring**: Mirror your Android device's screen on your PC.
- **Pointer Control**: Control Android device's screen from your PC.
- **Control Navigation**: Use your PC to navigate through your mobile device.
- **Music Control**: Play, pause, skip, and go back to the previous song.
- **Call Control**: Answer and hang up calls.
- **Test Cases**: Automatically test the above features.

![Screenshot 2024-07-11 093617](https://github.com/sumionochi/Android-Screen-Automation-Control-using-ABD/assets/89721628/e80e4644-fae2-4602-b2eb-435bbc06147c)

## Requirements

- Python 3.x
- ADB (Android Debug Bridge)
- OpenCV
- Tkinter

![Screenshot 2024-07-11 093556](https://github.com/sumionochi/Android-Screen-Automation-Control-using-ABD/assets/89721628/4562d11e-34f5-4d69-8046-a489010f3e40)

## Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/mobile-control.git
   cd mobile-control
   ```

2. **Install Dependencies:**
   ```bash
   pip install opencv-python-headless
   pip install opencv-python
   pip install pillow
   ```

3. **Connect to Your Android Device:**
   ```bash
   adb connect <device-ip>:<port>
   ```

## Usage

### Start Screen Mirroring

Run the main Python script to start the application:

```bash
python main.py
```

### Control Functions

- **Navigation:**
  - Left: `adb shell input keyevent 123`
  - Right: `adb shell input keyevent 124`
  - Up: `adb shell input keyevent 19`
  - Down: `adb shell input keyevent 20`
  
- **Music Control:**
  - Play/Pause: `adb shell input keyevent 85`
  - Next: `adb shell input keyevent 87`
  - Previous: `adb shell input keyevent 88`

- **Call Control:**
  - Answer/Hang Up: `adb shell input keyevent 5`
